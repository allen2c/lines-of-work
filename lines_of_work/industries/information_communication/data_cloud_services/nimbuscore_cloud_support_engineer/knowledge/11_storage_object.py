title = "Object Storage (NCS-S3) Troubleshooting"

content = """
- HTTP 403 on `PutObject` almost always maps to one of: bucket policy deny, missing `s3:PutObject` action in the IAM policy, or KMS key access denial for SSE-KMS buckets.
- HTTP 404 on `HeadObject` can mean the key does not exist OR the requester's IAM principal does not have `s3:ListBucket` on the prefix; both must be present for a successful check.
- Multipart upload threshold is 8 MB; uploads below this use a single PUT. If a customer complains about slow single-object uploads, check the part size first.
- Bucket versioning, once enabled, can only be suspended, not fully disabled. Reassure customers that existing delete markers remain recoverable.
- For accidental deletes, point the customer to the `nc-s3-undelete` self-service tool, which restores any object versioned within the last 30 days.
"""  # noqa: E501

version = "0.0.1"
