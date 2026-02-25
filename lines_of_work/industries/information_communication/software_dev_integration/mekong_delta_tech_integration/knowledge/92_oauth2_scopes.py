title = "OAuth2 Scopes"

content = """
Scope granular permission trong OAuth2. Client request scope. Server enforce.
Mekong Delta Tech design scope cho API access control.

**Design:** Resource:action. read:orders, write:users. Hoặc resource-only.
Granular. Document each scope. Principle of least privilege. Default minimal.

**Enforcement:** Check scope với mỗi request. Endpoint map to required scope.
403 khi insufficient. Validate scope at token issue. Don't over-grant. Refresh
token có same scope.

**Consent:** User consent per scope. Show scope to user. Revoke granular. Scope
change = re-consent. Clear. Don't surprise user. Audit scope grant.

**Integration:** Partner request scope. Review. Approve. Document. Monitor usage.
Detect scope creep. Regular review. Revoke unused.
"""  # noqa: E501

version = "0.0.1"
