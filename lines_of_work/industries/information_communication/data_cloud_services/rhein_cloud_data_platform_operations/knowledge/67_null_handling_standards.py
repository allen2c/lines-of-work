title = "Null-Behandlungsstandards"

content = """
Einheitliche Behandlung von NULL-Werten verhindert Inkonsistenzen. Standards: COALESCE
für Defaults, explizite NULL-Checks in Joins, Dokumentation ob NULL erlaubt ist.
Bei Aggregationen: NULL vs. 0 unterscheiden. In Schemas: Nullable-Flags und
Default-Werte definieren. Bei Exporten: NULL-Repräsentation (leer, N/A) festlegen.
"""

version = "0.0.1"
