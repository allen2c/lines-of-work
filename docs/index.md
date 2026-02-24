# Lines of Work — Documentation

## What Is This?

`lines-of-work` is a Python library of agent definitions, each scoped to one specific partial duty within a distinctively named entity — the concierge at a fantasy hotel, the code-review desk at a boutique studio, the admissions office at a named university. Each *work* ships with two resources:

- **Agent** — a persona prompt tightly scoped to one duty within one named entity, ready to plug into any LLM-powered agent framework.
- **Knowledge base** — a curated set of topical entries covering the domain expertise required to carry out that duty.

The library is organized as a three-level taxonomy:

```text
Industry  →  Subcategory  →  Work
```

All 19 industries and their subcategories are available out of the box. Work modules are added incrementally.

---

## Taxonomy

The full taxonomy is discoverable at runtime:

```python
import lines_of_work as low

industries    = low.list_industry_ids()
subcategories = low.list_subcategory_ids(low.IndustryID("finance_insurance"))
works         = low.list_work_ids(
    low.IndustryID("finance_insurance"),
    low.SubcategoryID("banking"),
)
```

Each call returns a plain list of typed string IDs (`IndustryID`, `SubcategoryID`, `WorkID`). No work modules are loaded until you explicitly construct a `Work`.

---

## Loading a Work

```python
work = low.Work(
    low.IndustryID("healthcare_social_work"),
    low.SubcategoryID("clinic_medical_services"),
    low.WorkID("silver_lotus_clinic_triage"),
)

# Agent
print(work.agent.name)          # "Silver Lotus Clinic — Triage"
print(work.agent.description)   # what entity + what duty
print(work.agent.instructions)  # persona prompt scoped to this duty (up to 2048 tokens)

# Knowledge
for kid in work.list_knowledge_ids():
    entry = work.get_knowledge(kid)
    print(entry.title)
    print(entry.content)
```

`Work` loads `agent.py` eagerly on construction. Knowledge items are loaded on demand via `get_knowledge`.

---

## Data Models

### `Agent`

| Field | Type | Description |
| --- | --- | --- |
| `name` | `str` | `"<Entity> — <Duty>"` (e.g. `"Fantasy Moon Hotel — Concierge"`). |
| `description` | `str` | What entity this belongs to and what specific duty this agent covers. |
| `instructions` | `str` | Persona prompt scoped to this duty within this entity. Up to 2048 tokens. |
| `version` | `str` | Semantic version, default `"0.0.1"`. |

### `Knowledge`

| Field | Type | Description |
| --- | --- | --- |
| `title` | `str` | Short topic heading. |
| `content` | `str` | Substantive text on the topic. 128–1024 tokens per item. |
| `version` | `str` | Semantic version, default `"0.0.1"`. |

### `Industry` / `Subcategory`

Both are Pydantic models with `id`, `name`, and `description` fields. `Industry` also carries a `subcategories: list[Subcategory]`. They can be populated by importing an industry or subcategory module directly:

```python
import importlib

ind = importlib.import_module("lines_of_work.industries.education")
print(ind.name)        # "Education"
print(ind.description)
```

---

## Module Layout

```text
lines_of_work/
├── __init__.py           # list_industry_ids, list_subcategory_ids,
│                         # list_work_ids, Work
├── types.py              # IndustryID, SubcategoryID, WorkID, KnowledgeID,
│                         # Agent, Knowledge, Industry, Subcategory
├── version.py
└── industries/
    └── <industry_id>/
        ├── __init__.py       # id, name, description
        └── <subcategory_id>/
            ├── __init__.py   # id, name, description
            └── <work_id>/
                ├── __init__.py
                ├── agent.py
                └── knowledge/
                    ├── __init__.py
                    └── <knowledge_id>.py
```

---

## Further Reading

- [Guide: Defining a New Work](guidance_of_new_work.md)
- [PyPI package](https://pypi.org/project/lines-of-work/)
- [GitHub repository](https://github.com/allen2c/lines-of-work)
