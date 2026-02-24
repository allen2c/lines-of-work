title = "Spec-first Development"

content = """
Spec-first: viết OpenAPI spec trước code. Contract làm source of truth. Client
và server develop song song. Mekong Delta Tech prefer spec-first cho public API.

**Workflow:** Design API trong spec. Review với stakeholder. Generate mock server.
Client develop against mock. Server implement to spec. Contract test verify.
Integration test. Release.

**Benefits:** Early feedback. Mock enable parallel work. Spec = documentation.
Avoid over/under designing. Client không chờ server. Reduce integration issue.

**Tooling:** OpenAPI editor. Mock server (Prism, Postman). Client generator.
Validation step trong CI. Spec trong repo. Version với API.

**Review:** Spec review như code review. Breaking change review carefully.
Stakeholder sign-off. Changelog trong spec. Deprecation in spec.
"""  # noqa: E501

version = "0.0.1"
