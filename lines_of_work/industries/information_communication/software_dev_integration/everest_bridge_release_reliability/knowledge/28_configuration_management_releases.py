"""Configuration management for releases."""

title = "Configuration Management in Releases"

content = """
Configuratie moet versioned en environment-specifiek zijn. Scheid secrets van
non-secret config. Gebruik config management tools (bijv. config servers, env vars)
en vermijd hardcoded waarden. Bij release: valideer dat benodigde config keys
aanwezig zijn. Documenteer config wijzigingen in release notes. Test config
in staging vóór productie.
"""

version = "0.0.1"
