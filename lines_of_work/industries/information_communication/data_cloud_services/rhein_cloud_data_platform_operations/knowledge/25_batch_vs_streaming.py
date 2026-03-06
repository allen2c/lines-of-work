title = "Batch vs Streaming Processing"

content = """
Batch processing handles data in scheduled chunks (hourly, daily); streaming
processes events as they arrive. Choose batch when latency in hours is acceptable,
sources are file- or API-based, and transformations are complex. Choose streaming
when sub-minute latency is required, sources emit events continuously, and
use cases need real-time dashboards or alerts. Hybrid architectures are common:
stream ingestion into a lake, then batch transformation. Rhein Cloud operates
both; operational decisions (scheduling, resource allocation) differ. Batch
failures can be retried; streaming requires backpressure and lag monitoring.
"""

version = "0.0.1"
