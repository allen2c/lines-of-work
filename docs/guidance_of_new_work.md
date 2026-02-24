# Guide: Defining a New Work

This document describes the file layout, naming rules, and content standards for adding a new work to `lines-of-work`.

---

## 1. Locate the Right Subcategory

Every work belongs to exactly one industry → subcategory pair. Use the existing taxonomy to find the best fit:

```python
import lines_of_work as low

print(low.list_industry_ids())
print(low.list_subcategory_ids(low.IndustryID("professional_scientific_tech")))
```

If no existing subcategory fits, open an issue before creating a new one. Do not invent industries or subcategories unilaterally.

---

## 2. Directory Structure

Create the following layout under the matching subcategory:

```text
lines_of_work/industries/<industry_id>/<subcategory_id>/<work_id>/
├── __init__.py
├── agent.py
└── knowledge/
    ├── __init__.py
    ├── <knowledge_id>.py
    ├── <knowledge_id>.py
    └── ...              (20 – 500 files)
```

All four items are mandatory. A work module missing any of them will load partially or raise errors at runtime.

---

## 3. Naming Conventions

### `work_id`

- **Format:** `snake_case`
- **Represents:** a cohesive set of related duties handled by an agent *within* a named entity — e.g. the front desk operations at a particular hotel, the loan and credit desk at a particular bank, the patient intake function at a particular clinic
- **Length:** 2–6 words joined with underscores; include both the entity name and the functional role area
- **Style:** evocative entity name + a clear role-area suffix; the suffix names a functional unit, not a single micro-task
- **Stable:** once published, IDs must not be renamed (consumers depend on them)

Good examples: `fantasy_moon_hotel_front_desk`, `neon_circuit_labs_engineering`, `azure_peak_university_admissions`, `iron_veil_security_operations`
Bad examples: `hotel_front_desk` (entity not named), `fantasy_moon_hotel` (role area not specified), `FantasyMoonFrontDesk` (wrong case)

### `knowledge_id`

- **Format:** `snake_case`
- **Represents:** a single, cohesive topic within the work's domain
- **Stable:** same rule as `work_id` — never rename after first release

Good examples: `design_patterns`, `data_structures`, `patient_communication`, `tax_code_overview`

---

## 4. `__init__.py`

The work-level `__init__.py` is empty. It exists solely to make the directory a Python package:

```python
# lines_of_work/industries/<industry_id>/<subcategory_id>/<work_id>/__init__.py
```

Likewise, `knowledge/__init__.py` is empty.

---

## 5. `agent.py` — Partial Duty Definition

`agent.py` defines the identity and operating scope of the agent handling **a cohesive set of related duties** within its parent entity. The agent is not the whole entity — it is a functional role area: the front desk, the engineering team, the admissions office, the patient intake unit. Duties grouped into one agent should share the same context, knowledge domain, and communication style. It is loaded eagerly when a `Work` object is constructed.

### Required module-level variables

```python
name: str          # "<Entity Name> — <Duty>" (e.g. "Fantasy Moon Hotel — Concierge")
description: str   # one or two sentences: what entity this belongs to and what duties this agent covers
instructions: str  # the full system-prompt scoped to these duties
language: str      # BCP 47 code for the agent's default operating language (e.g. "en", "zh-Hans")
version: str       # semantic version string, default "0.0.1"
```

### Choosing a Default Language

Every agent operates in one primary language. Choose the language that best matches the entity's real-world market and audience. The supported languages and their BCP 47 codes are:

| #  | Language                       | Code      | Primary Context                                                  |
|----|--------------------------------|-----------|------------------------------------------------------------------|
| 1  | English                        | `en`      | Global business, science, and the internet                       |
| 2  | Mandarin Chinese (Simplified)  | `zh-Hans` | Mainland China, Singapore, global supply chains                  |
| 3  | Spanish                        | `es`      | Latin American markets, US Hispanic population                   |
| 4  | French                         | `fr`      | Diplomacy, high-growth emerging markets in Africa                |
| 5  | Mandarin Chinese (Traditional) | `zh-Hant` | Taiwan semiconductors, Hong Kong finance, overseas communities   |
| 6  | German                         | `de`      | European engineering, manufacturing, EU economy                  |
| 7  | Arabic                         | `ar`      | Energy sectors, sovereign wealth funds, Middle Eastern diplomacy |
| 8  | Japanese                       | `ja`      | R&D, robotics, automotive, global media                          |
| 9  | Hindi                          | `hi`      | India's domestic market and tech outsourcing                     |
| 10 | Portuguese                     | `pt`      | Brazil's commodities and South American trade                    |
| 11 | Russian                        | `ru`      | Energy, aerospace, Central Asian influence                       |
| 12 | Korean                         | `ko`      | Consumer electronics, semiconductors, global entertainment       |
| 13 | Italian                        | `it`      | Luxury goods, fashion, industrial design, culinary               |
| 14 | Bengali                        | `bn`      | South Asian demographics, textile and manufacturing              |
| 15 | Indonesian                     | `id`      | Southeast Asia's largest economy, digital markets                |
| 16 | Turkish                        | `tr`      | Europe–Asia bridge, regional logistics and construction          |
| 17 | Vietnamese                     | `vi`      | Manufacturing shift, global supply chains                        |
| 18 | Urdu                           | `ur`      | South Asian trade and diaspora networks                          |
| 19 | Swahili                        | `sw`      | East African trade, one of the fastest-growing regions           |
| 20 | Thai                           | `th`      | Tourism, automotive manufacturing, Southeast Asian logistics     |
| 21 | Polish                         | `pl`      | Central and Eastern European manufacturing and logistics         |
| 22 | Dutch                          | `nl`      | International maritime trade, European legal and logistics hubs  |

If the entity genuinely operates in multiple languages (e.g. a multilingual UN agency), choose the language of its primary operating context and note the others in `description`. Do not attempt to cover multiple languages in a single `agent.py` — create separate work modules for each language variant instead.

### Minimal template

```python
name = "Neon Circuit Labs — Code Review"

description = (
    "The code review agent for Neon Circuit Labs, a boutique software research studio. "
    "This agent handles pull-request feedback, enforces the studio's engineering standards, "
    "and guides contributors toward production-ready submissions."
)

instructions = """
You are the code review agent for Neon Circuit Labs — a boutique software research
studio known for precision engineering and open-source tooling. Your duties cover
the full engineering workflow: code review, technical design feedback, and
implementation guidance for contributors and internal engineers.

## Scope of Duties
You handle code reviews, pull-request feedback, architecture discussions within
active work items, and implementation guidance. You do not manage deployments,
respond to user support tickets, or make product roadmap decisions.

## Review Standards
...

## Tone and Feedback Style
...

## What to Approve, Request Changes On, and Reject
...

## Escalation
...
"""

language = "en"

version = "0.0.1"
```

### Content standards for `instructions`

| Property       | Requirement                                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Token budget   | **Up to 2048 tokens** (~1500 words). Aim for this ceiling — richer prompts produce better-calibrated agents. |
| Minimum length | 512 tokens (~380 words). Sparse instructions are rejected.                                                   |
| Tone           | First-person, authoritative, professional.                                                                   |
| Structure      | Use Markdown headings (`##`) to organize sections.                                                           |

**Recommended sections** (adapt as appropriate for the role area):

1. **Scope of Duties** — what this agent is responsible for and, equally important, what it is *not* responsible for.
2. **Parent Entity Context** — a brief description of the entity this role belongs to, so the agent can speak in character.
3. **Core Tasks** — the 5–10 specific actions this agent performs across its duties.
4. **Domain Knowledge Required** — the expertise needed to carry out these duties well.
5. **Tone and Communication Style** — how this agent speaks to the people it serves.
6. **Decision Criteria** — how the agent evaluates requests, prioritizes, or makes judgments within its scope.
7. **Escalation and Handoff** — what falls outside these duties and how to direct it appropriately.

The goal is a prompt scoped tightly enough that the agent knows exactly what it is responsible for, and rich enough that it can handle any task within those duties accurately and in character.

---

## 6. `knowledge/<knowledge_id>.py` — Knowledge Items

Each file in `knowledge/` represents one discrete topic. The collection constitutes the domain expertise and operational knowledge that defines this type of entity.

### Required module-level variables (Knowledge)

```python
title: str    # short heading for the topic
content: str  # substantive prose on the topic
version: str  # semantic version string, default "0.0.1"
```

### Minimal template (Knowledge)

```python
title = "Guest Check-In and Room Assignment Protocols"

content = """
The check-in process is the first direct touchpoint between the hotel and its
guests, and it sets the tone for the entire stay. A well-run check-in is swift,
warm, and anticipates needs before they are voiced.

**Identity Verification:** Confirm the guest's name against the reservation and
request a valid government-issued photo ID. For international guests, a passport
is standard; domestic guests may present a national ID or driver's license.

**Room Assignment:** Cross-reference the reservation against current room
availability before assigning. Upgrades should be offered proactively when a
room of a higher category is vacant and the guest's profile or loyalty tier
warrants it.

**Key Issuance:** Issue two keycards by default. Program the keycard immediately
at the desk and confirm functionality before the guest leaves the lobby. Avoid
announcing the room number aloud in a crowded lobby.

**Special Requests:** Review the reservation notes for pre-arranged items such
as early check-in, accessibility requirements, crib or rollaway needs, or
welcome amenities. Confirm these are fulfilled before escorting the guest or
directing them to their floor.

**Payment and Authorization:** Collect a credit card authorization for incidentals
at check-in. Clearly communicate the authorization amount and explain that it is
a hold, not a charge, released upon checkout.
"""

version = "0.0.1"
```

### Content standards for individual items

| Property              | Requirement                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------|
| Token budget per item | **128 – 1024 tokens** (~96 – 768 words)                                                    |
| Minimum               | 128 tokens. Items shorter than this lack sufficient depth.                                 |
| Maximum               | 1024 tokens. Exceed this by splitting into two focused items.                              |
| Tone                  | Explanatory, factual, professional. Written as reference material, not a tutorial.         |
| Self-contained        | Each item must make sense independently. Do not assume the reader has read adjacent items. |
| No duplication        | Each `knowledge_id` should cover a distinct concept. Overlapping items dilute quality.     |

### Collection standards

| Property      | Requirement                                                                                                                                                                                                                   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum items | **20** per work                                                                                                                                                                                                               |
| Maximum items | **500** per work                                                                                                                                                                                                              |
| Coverage      | Items should span the full breadth of the role — foundational concepts, advanced techniques, tools, processes, regulations, soft skills, and common failure modes.                                                            |
| Ordering      | IDs are discovered alphabetically from the filesystem. Design IDs so that alphabetical order produces a coherent reading sequence when useful (e.g., prefix with a two-digit number: `01_foundations`, `02_data_structures`). |

### Suggested coverage areas (adapt per entity type)

- Foundational domain theory and concepts
- Core services, products, or operational methods
- Industry-standard processes and workflows
- Regulatory and compliance requirements for this type of entity
- Common failure modes and how the entity handles them
- Client or customer interaction patterns
- Quality standards and performance benchmarks
- Internal culture, values, and working norms

---

## 7. Versioning

All three version fields (`agent.py`, each `knowledge/*.py`) default to `"0.0.1"`. Follow semantic versioning when updating existing content:

- **Patch** (`0.0.x`): typo fixes, minor clarifications that do not change meaning.
- **Minor** (`0.x.0`): substantive content additions or expansions.
- **Major** (`x.0.0`): fundamental rewrites or changes that alter the semantics of the role definition.

Consumers may depend on version strings to cache or invalidate loaded content.

---

## 8. Pre-submission Checklist

Before opening a pull request, confirm all of the following:

- [ ] `work_id` is `snake_case`, follows `<entity>_<role_area>` format, and uniquely identifies this agent within its subcategory.
- [ ] `agent.py` is present with all five variables (`name`, `description`, `instructions`, `language`, `version`).
- [ ] `language` is a valid BCP 47 code from the supported language list.
- [ ] `instructions` is between 512 and 2048 tokens.
- [ ] `knowledge/__init__.py` is present (empty).
- [ ] At least 20 knowledge items exist.
- [ ] Every knowledge item is between 128 and 1024 tokens.
- [ ] No two knowledge items cover the same concept.
- [ ] All `knowledge_id` filenames are `snake_case`.
- [ ] All files use `version = "0.0.1"` (or a higher version if updating existing content).
- [ ] The work is importable: `python -c "import lines_of_work as low; low.Work('<industry_id>', '<subcategory_id>', '<work_id>')"` runs without error.
