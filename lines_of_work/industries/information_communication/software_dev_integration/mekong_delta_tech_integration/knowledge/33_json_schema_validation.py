title = "JSON Schema Validation"

content = """
JSON Schema mô tả cấu trúc JSON. Dùng để validate request/response, generate
documentation, code. Mekong Delta Tech validate API payload với JSON Schema.

**Schema Definition:** properties, required, type, format, enum, pattern.
Nested objects. Array với items schema. $ref để reuse. additionalProperties
để allow/disallow extra fields.

**Validation Library:** ajv (JavaScript), jsonschema (Python), many others.
Validate trước khi process. Fail fast với clear error. Return validation error
với path (field level). User-friendly message.

**Schema Evolution:** Adding optional property: backward compatible. Removing or
changing type: breaking. Version schema. Validate với both old and new khi
transition. Generate migration guide.

**Performance:** Compile schema once. Validate in middleware. Schema complexity
ảnh hưởng validation speed. Benchmark cho high-throughput API. Consider
validation skip cho internal trusted service.
"""  # noqa: E501

version = "0.0.1"
