"""Backward compatibility verification."""

title = "Backward Compatibility Checks"

content = """
Backward compatibility voorkomt dat bestaande clients of integraties breken. Voer
compatibility tests uit: API contract tests, database schema checks, config format
validatie. Gebruik consumer-driven contract tests voor API's. Bij database wijzigingen:
valideer dat oude code werkt met nieuwe schema (indien ondersteund). Documenteer
compatibility guarantees per release.
"""

version = "0.0.1"
