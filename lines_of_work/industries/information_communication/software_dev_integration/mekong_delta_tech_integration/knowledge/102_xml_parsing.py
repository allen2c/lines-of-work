title = "XML Parsing"

content = """
XML parsing có security risk (XXE, billion laughs). Integration với SOAP,
legacy. Mekong Delta Tech parse XML safely.

**XXE Prevention:** Disable external entity. Disable DTD khi có thể. Use
parser với secure default. libxml2: LIBXML_NOENT off. Don't trust input.
Validate. Test với XXE payload.

**Billion Laughs:** Recursive entity expansion. Limit entity expansion.
Parser config. Limit depth. Limit size. Reject malicious. DoS prevention.

**Schema Validation:** Validate against XSD. Reject invalid. Before process.
Schema from trusted source. Don't fetch schema from input. Cache schema.

**Performance:** Large XML use streaming. SAX, pull parser. Don't load entire
DOM. Memory bound. Suitable for integration. Trade-off flexibility.
"""  # noqa: E501

version = "0.0.1"
