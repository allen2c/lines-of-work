title = "OpenAPI Specification"

content = """
OpenAPI (Swagger) mô tả REST API dưới dạng YAML/JSON. Toolchain rộng: doc gen,
client gen, validation, mock. Mekong Delta Tech dùng OpenAPI cho mọi public API.

**Structure:** paths, components (schemas, responses), servers, security. Reuse
schema với $ref. Tag để group operation. Description cho mọi element.

**Schema Definition:** Request/response body schema. Required vs optional. Enum,
format, validation. Example values. Nested objects. Array items schema.

**Code Generation:** openapi-generator hoặc類似 tool. Generate client SDK nhiều
language. Keep spec as source of truth. Regenerate on change. Version SDK với API.

**Validation:** Validate request against spec at runtime (optional). Validate spec
syntax (swagger-cli). Contract test với generated types. Spec quality = API quality.
"""  # noqa: E501

version = "0.0.1"
