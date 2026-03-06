title: str = "dbt und die Transformation Layer"

content: str = """
dbt (data build tool) ist ein Framework für Transformationen im Data
Warehouse. Es nutzt SQL und Jinja-Templating, um modulare, versionierte
und testbare Transformationen zu definieren.

**Modelle:** Jede SQL-Datei im models-Ordner wird zu einem Modell
kompiliert. Modelle referenzieren einander via ref(); dbt baut den
DAG der Abhängigkeiten automatisch.

**Tests:** Schema-Tests (unique, not_null, accepted_values) und
Custom Data-Tests prüfen die Qualität. Tests laufen nach dem Build.

**Inkrementelle Modelle:** incremental-Strategien (append, merge)
verarbeiten nur neue Daten und reduzieren Laufzeit und Kosten.

**Dokumentation:** YAML-Dateien dokumentieren Modelle und Spalten;
dbt generiert eine webbasierte Dokumentation mit Lineage.
"""

version: str = "0.0.1"
