title = "JSON Parsing An toàn"

content = """
JSON parsing có thể vulnerable (billion laughs, deep nesting). Large payload.
Integration parse JSON từ untrusted source. Mekong Delta Tech parse safely.

**Size Limit:** Limit payload size. Reject oversized. Prevent DoS. Config
max. Document. Apply at gateway. Per-endpoint có thể khác.

**Depth Limit:** Limit nesting depth. Deeply nested = stack overflow risk.
Reject hoặc truncate. Typical limit 32-64. Parser config. Test.

**Number:** BigInteger, float precision. Parser handle. Don't trust number
range. Validate after parse. Integer overflow. Decimal for money.

**Streaming:** Large JSON use streaming parser. Don't load entire vào memory.
SAX-style. Process incrementally. Memory bound. Trade-off complexity.
"""  # noqa: E501

version = "0.0.1"
