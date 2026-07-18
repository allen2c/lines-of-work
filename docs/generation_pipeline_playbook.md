# Large-Scale Content Generation Pipeline — Playbook & Lessons

A reusable methodology for producing a large, structured, multilingual content
library at scale, using cloud generation models with automated quality gating
and script-based materialization. This document captures the architecture and
the engineering lessons learned so the approach can be reproduced or adapted.

## 1. Architecture

The pipeline runs as four stages, orchestrated from shell (no long-lived
services). Each stage is independently restartable.

```
  headers ─▶ generate ─▶ review/repair ─▶ materialize ─▶ verify
 (specs)   (N models)   (LLM-as-judge)    (script)     (load+test+fmt)
```

1. **Headers / specs** — one small spec per item (target category, language,
   role/topic hint, item count). Batched into a single file write.
2. **Generate** — one model call per item, emitting a **delimited draft** (see
   §3). Calls run concurrently with a capped fan-out.
3. **Review / repair** — a deterministic pre-check computes objective facts
   (counts, tokens, language, structural markers); an LLM reviewer then judges
   format + quality and returns a machine-readable verdict. Failures are
   auto-repaired for a bounded number of rounds, then escalated.
4. **Materialize** — a small script parses each approved draft and writes the
   final files. Pure mechanical transform; idempotent and re-runnable.
5. **Verify** — programmatic load of every module + test suite + formatter as a
   **hard gate**. The batch is not "done" until this is green.

## 2. Key techniques

- **Delimited draft format over JSON.** Free-form generation into a
  line-delimited block (clear `BEGIN`/`END` and section markers) is far more
  robust than asking a model for strict JSON, especially across languages and
  long outputs. Parse with tolerant regexes.
- **Multi-model rotation for diversity.** Rotating several generation models
  across a batch produces genuinely different structure and voice, which raises
  corpus variety. Keep a fast, band-friendly model as the workhorse and use
  richer/slower models as a minority "accent" — they add depth but tend to run
  long and slow, so cap their share.
- **LLM-as-judge with a deterministic floor.** Feed the reviewer machine-measured
  facts alongside the draft so it does not have to *guess* counts or lengths.
  Validate that a negative control is actually caught before trusting PASSes —
  a reviewer that never fails is worthless.
- **Bounded auto-repair, then escalate.** On a failed review, send the issue list
  back for a corrected draft and re-review, up to K rounds. Only escalate to a
  human/expensive path when automated repair genuinely can't fix it. This keeps
  cost proportional to difficulty.
- **Script materialization beats agents for mechanical work.** Moving approved
  content into files is a deterministic transform — a ~150-line script does it
  for near-zero marginal cost. Reserve expensive agent runs for genuinely
  judgment-heavy steps.
- **Verification is the only source of truth.** Soft heuristics (token bands,
  style) inform; the programmatic load + test + format gate decides.

## 3. Draft format

A single delimited block per item, e.g.:

```
===ITEM===
ID: <snake_case ascii>
NAME: <display name>
LANGUAGE: <BCP47 base code>
---DESCRIPTION---
...
---BODY---
...(structured markdown)...
---SECTIONS---
[[01_slug]] <title>
<content>
[[02_slug]] <title>
...
===END===
```

Keep the parser tolerant: models drift on delimiters and casing (see §5).

## 4. Concurrency & rate limits

- Generation fan-out of ~16 concurrent calls was stable; a **burst of ~24
  concurrent review calls with long payloads triggered rate limiting (429)**.
  Cap the heavier stage lower (~12) and stagger.
- Put **exponential backoff on 429/503** in every network helper (e.g.
  10s → 40s → 90s …). It should be a safety net, not the primary throttle.
- On a partial failure (incomplete outputs), re-run only the missing items at
  reduced concurrency (halve, then serialize) rather than redoing the batch.

## 5. Gotchas (all cheap to hit, cheap to prevent)

- **Shell portability.** In `zsh`, `for x in $var` does **not** word-split an
  unquoted variable — the loop runs once with the whole string. Use an explicit
  literal list or an array.
- **Identifier constraints.** A module directory name used as a package cannot
  start with a digit. Scan generated IDs and rename (`24x` → `x24`).
- **Non-ASCII filenames are usually fine.** File-path-based module loading
  tolerates non-ASCII (and even hyphens) in filenames, so localized slugs load
  correctly — don't waste effort transliterating. But hyphens/spaces/dots in a
  name that must be an importable identifier are still hazards; flag them.
- **Delimiter & casing drift.** Models occasionally emit a variant marker
  (`===SECTION===` vs `---SECTION---`) or lowercase a field key. Make boundary
  regexes accept both, and extract keys case-insensitively.
- **Silent parse drops.** If a parser regex is too strict (e.g. ASCII-only slug
  match against localized slugs), it can silently yield *zero* items. Always
  assert parsed-count == expected-count and re-run mismatches.
- **Language contamination.** Cross-language leakage (a stray word from another
  script) is the most common quality defect; a targeted reviewer check catches
  it, and trivial cases can be fixed with a direct substitution instead of a
  full regeneration.
- **Length bands: soft vs hard.** Token-dense languages naturally run long;
  terse languages run short. Treat band edges as *soft* advisories and let the
  load/test/format gate be the hard failure. But watch verbose models — a single
  item ballooning far past the ceiling is worth regenerating with a leaner model.

## 6. Budget, resumability & note-keeping

- **Prefer scripts over agents for anything mechanical** — it is the single
  biggest cost lever.
- **Stages are restartable.** If a run is interrupted mid-batch, inspect the
  filesystem to find partially materialized items (`count files per module`) and
  finish only those.
- **Keep an append-only ledger** of progress (total after each batch) plus a
  compact index that points to detailed topic notes, rather than one growing
  log. It keeps the working context small and makes resumption trivial.

## 7. Per-batch checklist

1. Write the batch of headers in one file.
2. Assign a model per item (rotation) and fetch drafts concurrently; assert
   each draft has the expected item count and end marker.
3. Review at capped concurrency; auto-repair; escalate only stubborn failures.
4. Validate IDs (leading digit, casing, count, delimiter variant).
5. Materialize via the script; assert parsed-count per item; re-run mismatches.
6. Run the hard gate (load + tests + formatter); update the ledger.
