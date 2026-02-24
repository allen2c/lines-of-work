title = "Đặt tên REST Resource"

content = """
REST resource naming ảnh hưởng API clarity. Convention. Mekong Delta Tech
follow naming best practice. Consistent. Predictable.

**Nouns not Verbs:** /users not /getUsers. Resource-oriented. Action = HTTP
method. GET /users, POST /users. Clear. RESTful. Document.

**Plural:** /users not /user. Collection. Singular cho singleton (/me). 
Nested: /users/123/orders. Hierarchy. Limit depth. 2-3 level. Flatten khi
cần. Document.

**Lowercase, Hyphen:** users, order-items. No camelCase in URL. Hyphen.
Readable. No underscore (some disagree). Consistent. Document. Validate.

**Avoid:** Verb. Deep nesting. Extension (.json). Version in resource (use
path prefix). Clear. Simple. Predictable. Developer friendly.
"""  # noqa: E501

version = "0.0.1"
