title = "Field Selection"

content = """
Field selection (sparse fieldsets) cho phép client request chỉ fields cần thiết.
Giảm payload, bandwidth. Optional feature cho resource-heavy API. Mekong Delta
Tech support fields param cho GET.

**Syntax:** ?fields=id,name,email. Hoặc ?fields[user]=name,email&fields[order]=total.
Nested resource. Comma-separated. Document available fields. Reject invalid field.

**Security:** Chỉ expose field client có quyền. Filter field list by permission.
Don't expose internal field. Field cho PII có extra check. Validate against
schema. No arbitrary field injection.

**Implementation:** Query builder select specified columns. Reduce DB load.
Join optimization. Default fields khi không specify. Consider performance —
many fields với relation = N+1 risk. Provide field sets (views) cho common case.
"""  # noqa: E501

version = "0.0.1"
