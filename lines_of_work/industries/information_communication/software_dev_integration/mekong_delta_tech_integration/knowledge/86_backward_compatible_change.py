title = "Thay đổi tương thích ngược"

content = """
Backward compatible change không break client cũ. Additive: thêm field, endpoint.
Never remove, never change type. Mekong Delta Tech ưu tiên compatible change.

**Safe Additions:** Optional field. New endpoint. New value trong enum (client
ignore unknown). New optional parameter. Extend format. Document.

**Unsafe:** Remove field. Change type. Change meaning. Remove enum value.
Change required to optional (OK). Optional to required (breaking). Rename.
Change default. All require version.

**Testing:** Run old client against new server. Run new client against old
server (forward compatibility). Contract test. Compatibility suite. CI. Before
release.

**Communication:** Changelog. Deprecation when remove needed. Timeline. Give
client time. Support. Migration guide. Version API for big change.
"""  # noqa: E501

version = "0.0.1"
