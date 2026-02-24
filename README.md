# Lines of Work

[![PyPI version](https://img.shields.io/pypi/v/lines-of-work.svg)](https://pypi.org/project/lines-of-work/)
[![Python Version](https://img.shields.io/pypi/pyversions/lines-of-work.svg)](https://pypi.org/project/lines-of-work/)
[![License](https://img.shields.io/pypi/l/lines-of-work.svg)](https://opensource.org/licenses/MIT)

A structured Python library of agent definitions, each covering a cohesive set of related duties within a distinctively named entity — organized by industry and subcategory, each shipping with a focused persona prompt and a curated knowledge base.

## Documentation

- [Overview](docs/index.md)
- [Guide: Defining a New Work](docs/guidance_of_new_work.md)

## Installation

```bash
pip install lines-of-work
```

## Quick Start

```python
import lines_of_work as low

# Enumerate the taxonomy
industries = low.list_industry_ids()
subcategories = low.list_subcategory_ids(low.IndustryID("information_communication"))
works = low.list_work_ids(
    low.IndustryID("information_communication"),
    low.SubcategoryID("software_dev_integration"),
)

# Load a work
work = low.Work(
    low.IndustryID("information_communication"),
    low.SubcategoryID("software_dev_integration"),
    low.WorkID("neon_circuit_labs_code_review"),
)

print(work.agent.name)
print(work.agent.instructions)

for kid in work.list_knowledge_ids():
    k = work.get_knowledge(kid)
    print(k.title, "—", k.content[:80])
```

## Public API

All symbols below are importable directly from `lines_of_work`.

### Enumeration

| Function               | Signature                                     | Description                         |
|------------------------|-----------------------------------------------|-------------------------------------|
| `list_industry_ids`    | `() -> list[IndustryID]`                      | All available industry IDs.         |
| `list_subcategory_ids` | `(IndustryID) -> list[SubcategoryID]`         | Subcategory IDs within an industry. |
| `list_work_ids`        | `(IndustryID, SubcategoryID) -> list[WorkID]` | Work IDs within a subcategory.      |

### Work

```python
work = low.Work(industry_id, subcategory_id, work_id)
```

| Attribute / Method          | Type / Signature             | Description                            |
|-----------------------------|------------------------------|----------------------------------------|
| `work.agent`                | `Agent`                      | Agent metadata loaded from `agent.py`. |
| `work.list_knowledge_ids()` | `() -> list[KnowledgeID]`    | Knowledge item IDs.                    |
| `work.get_knowledge(kid)`   | `(KnowledgeID) -> Knowledge` | Load one knowledge item.               |

### Types

| Symbol          | Kind           | Description                                       |
|-----------------|----------------|---------------------------------------------------|
| `IndustryID`    | `NewType(str)` | Identifier for an industry.                       |
| `SubcategoryID` | `NewType(str)` | Identifier for a subcategory.                     |
| `WorkID`        | `NewType(str)` | Identifier for a work.                            |
| `KnowledgeID`   | `NewType(str)` | Identifier for a knowledge item.                  |
| `Agent`         | Pydantic model | `name`, `description`, `instructions`, `version`. |
| `Knowledge`     | Pydantic model | `title`, `content`, `version`.                    |
| `Subcategory`   | Pydantic model | `id`, `name`, `description`.                      |
| `Industry`      | Pydantic model | `id`, `name`, `description`, `subcategories`.     |

## Taxonomy

19 industries, each containing between 2 and 7 subcategories.

| Industry ID                     | Name                                                 |
|---------------------------------|------------------------------------------------------|
| `agriculture_natural_resources` | Agriculture and Natural Resources                    |
| `manufacturing_light`           | Manufacturing (Light Industry)                       |
| `manufacturing_heavy_tech`      | Manufacturing (Heavy and Tech Industry)              |
| `energy_utilities`              | Energy and Utilities                                 |
| `construction_civil_eng`        | Construction and Civil Engineering                   |
| `wholesale_retail`              | Wholesale and Retail Trade                           |
| `transportation_warehousing`    | Transportation and Warehousing                       |
| `accommodation_food_services`   | Accommodation and Food Services                      |
| `information_communication`     | Information and Communication                        |
| `finance_insurance`             | Finance and Insurance                                |
| `real_estate`                   | Real Estate                                          |
| `professional_scientific_tech`  | Professional, Scientific, and Technical Services     |
| `administrative_support`        | Administrative and Support Services                  |
| `public_admin_defense`          | Public Administration and Defense                    |
| `education`                     | Education                                            |
| `healthcare_social_work`        | Healthcare and Social Assistance                     |
| `arts_entertainment_recreation` | Arts, Entertainment, and Recreation                  |
| `other_services`                | Other Services                                       |
| `international_organizations`   | International Organizations and Foreign Institutions |

## Module Layout

```text
lines_of_work/
├── __init__.py           # Public API
├── types.py              # ID types and Pydantic models
├── version.py
└── industries/
    └── <industry_id>/
        ├── __init__.py   # id, name, description
        └── <subcategory_id>/
            ├── __init__.py   # id, name, description
            └── <work_id>/
                ├── __init__.py
                ├── agent.py          # name, description, instructions, version
                └── knowledge/
                    ├── __init__.py
                    └── <knowledge_id>.py  # title, content, version
```

## Contributing

See [Guide: Defining a New Work](docs/guidance_of_new_work.md) for content standards and file conventions.

## License

MIT
