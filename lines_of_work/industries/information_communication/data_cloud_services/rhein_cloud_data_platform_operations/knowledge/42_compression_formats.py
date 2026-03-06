title = "Kompressionsformate für Datenobjekte"

content = """
Die Wahl des Kompressionsformats beeinflusst Speicherbedarf, Lese- und
Schreibgeschwindigkeit. Parquet mit Snappy ist Standard für analytische Workloads.
GZIP bietet höhere Kompression bei langsamerer Verarbeitung. Zstd balanciert
beides. Für Streaming-Daten wird oft keine Kompression oder LZ4 verwendet.
Rhein Cloud empfiehlt Parquet+Snappy für Data Lakes und Delta-Tabellen. Bei
archivierten Daten kann GZIP sinnvoll sein. Die Kompression muss mit dem
zugrunde liegenden Dateiformat kompatibel sein.
"""

version = "0.0.1"
