title = "Phiên bản hóa API"

content = """
API versioning cho phép evolution mà không break client hiện tại. Strategy versioning
ảnh hưởng maintainability và developer experience.

**URL Versioning:** /v1/users, /v2/users. Rõ ràng, dễ cache, dễ routing. Phổ biến nhất.
Support nhiều version song song trong transition period.

**Header Versioning:** Accept: application/vnd.api+v1+json. URL sạch. Nhưng khó
test và cache. Ít phổ biến hơn.

**Breaking vs Non-Breaking:** Non-breaking: thêm optional field, endpoint mới. Breaking:
xóa field, đổi type, đổi behavior. Breaking change = major version mới. Communicate
deprecation timeline.

**Deprecation Policy:** Thông báo trước 6-12 tháng. Sunset header trong response.
Document migration path. Monitor usage của version cũ. Final deprecation và remove.
"""  # noqa: E501

version = "0.0.1"
