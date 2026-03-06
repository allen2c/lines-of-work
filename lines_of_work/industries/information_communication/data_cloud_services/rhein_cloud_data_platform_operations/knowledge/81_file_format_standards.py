title = "File Format Standards"

content = """
Rhein Cloud standardizes on Parquet for analytical data, JSON for events, and
CSV only for legacy compatibility. Parquet provides compression and schema
evolution. Choose partitioning and compression (Snappy, Zstd) per use case.
Avoid proprietary formats that limit portability. Document format choices
in data contracts.
"""

version = "0.0.1"
