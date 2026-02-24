title = "Unicode và Encoding"

content = """
Vietnamese text (dấu, tiếng Việt) require proper Unicode. Integration phải handle
encoding correct. Mekong Delta Tech enforce UTF-8 everywhere.

**UTF-8 Default:** All API, DB, file use UTF-8. Content-Type: charset=utf-8.
DB collation utf8mb4. Validate input là valid UTF-8. Reject invalid sequence.

**Normalization:** Unicode normalization (NFC, NFD). Consistent normal form.
Avoid duplicate (cafe vs café). Compare normalized. Store normalized.

**Legacy:** Legacy system có thể dùng TCVN3, VNI. Convert khi integrate.
Migration path. Document encoding. Test với Vietnamese text. Edge case:
emoji, rare character.

**API:** Accept UTF-8. Return UTF-8. Document. Client encode correct. No
encoding loss. Test với full Vietnamese charset.
"""  # noqa: E501

version = "0.0.1"
