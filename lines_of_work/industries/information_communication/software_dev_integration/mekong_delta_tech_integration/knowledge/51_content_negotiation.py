title = "Content Negotiation"

content = """
Content negotiation cho phép client request format ưa thích (JSON, XML). Server
trả về format phù hợp. Mekong Delta Tech support JSON primary, XML cho legacy.

**Accept Header:** Accept: application/json, application/xml;q=0.9. Quality value
q. Server pick best match. Default khi không có Accept. Document supported types.

**Content-Type:** Request body format. Content-Type: application/json. Server
validate. Reject unsupported với 415. Response Content-Type match body format.

**Version in Accept:** application/vnd.api+v1+json. Version và format combined.
Cho phép version negotiation. Client explicit về format và version cần.

**Charset:** UTF-8 default. Accept-Charset. Specify trong Content-Type. Handle
encoding correct. Vietnamese text require UTF-8. Validate input encoding.
"""  # noqa: E501

version = "0.0.1"
