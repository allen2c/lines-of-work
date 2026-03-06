title = "Feature Flags and Data Flows"

content = """
Feature flags can affect which data paths are active. When a feature flag
changes, downstream pipelines may receive different volumes or schemas.
Operations must track flag state and pipeline dependencies. Gradual rollouts
require monitoring for data skew. Disabled features should not block critical
pipelines. Document flag-to-pipeline mappings in the data catalog.
"""

version = "0.0.1"
