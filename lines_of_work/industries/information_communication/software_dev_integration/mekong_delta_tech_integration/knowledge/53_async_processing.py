title = "Xử lý bất đồng bộ"

content = """
Long-running operation không block response. Return 202 Accepted, process async.
Client poll hoặc nhận callback. Mekong Delta Tech dùng async cho operation > 5s.

**202 Response:** Immediate 202. Location header với status URL. Body có job_id
hoặc task_id. Client poll status URL. Document poll interval. Rate limit poll.

**Status Endpoint:** GET /jobs/{id} trả status (pending, processing, completed,
failed). Result khi completed. Error info khi failed. TTL cho job record.

**Webhook Callback:** Option: server call client webhook khi done. Client provide
callback URL. Same as async webhook. Verify webhook. Retry delivery.

**Idempotency:** Async request có idempotency key. Same key = same job. Return
existing job status. Don't create duplicate job. Cleanup old jobs.
"""  # noqa: E501

version = "0.0.1"
