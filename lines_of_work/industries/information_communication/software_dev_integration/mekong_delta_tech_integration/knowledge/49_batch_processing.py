title = "Batch Processing"

content = """
Batch processing xử lý large volume offline. Phù hợp cho ETL, report, sync.
Khác real-time — latency cao hơn nhưng throughput tốt. Mekong Delta Tech dùng
batch cho nhiều integration scenarios.

**Job Design:** Chunk large dataset. Process chunk. Checkpoint progress. Resume
from checkpoint khi fail. Parallel chunks khi có thể. Idempotent chunk processing.

**Scheduling:** Cron, workflow engine (Airflow). Schedule off-peak. Consider
dependency (B sau A). Retry policy. Alert on failure. Monitor duration.

**Resource:** Batch có thể resource-intensive. Separate pool. Scale worker.
Memory limit. Avoid OOM. Consider serverless (Lambda batch) cho variable load.

**Observation:** Log progress. Metrics: items processed, duration, error count.
Dashboard. Alert when batch duration tăng đột biến. Data quality checks.
"""  # noqa: E501

version = "0.0.1"
