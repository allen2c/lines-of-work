title = "Transfer file"

content = """
File transfer (upload, download) là integration pattern. FTP, SFTP, S3, API
multipart. Mekong Delta Tech support multiple file transfer methods.

**Upload:** Multipart form data. Chunk upload cho large file. Resumable.
Verify checksum. Virus scan. Size limit. Type restriction. Temporary store,
process async. Cleanup after.

**Download:** Direct URL (signed) hoặc stream. Range request cho partial.
CDN cho large file. Expire link. Don't proxy large file qua app server.

**SFTP/FTP:** Legacy integration. Batch file exchange. Poll directory. Process
file. Move to processed. Error handling. Retry. Idempotent processing (filename
unique). Secure (SFTP over SSH). Credential management.
"""  # noqa: E501

version = "0.0.1"
