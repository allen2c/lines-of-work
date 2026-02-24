title = "Integration Testing"

content = """
Integration test verify các component làm việc cùng nhau đúng. Khác unit test —
test interaction thật (hoặc test double có kiểm soát).

**Test Scope:** Test API endpoint với DB thật hoặc container. Test message flow
qua queue. Test auth flow. Tránh test toàn bộ system (đó là E2E).

**Test Data:** Isolated data per test. Seed database. Cleanup after. Có thể dùng
transaction rollback. Tránh shared state giữa tests.

**Test Doubles:** Mock external service khi cần (third-party API). Use WireMock
hoặc similar cho HTTP. Stub Kafka. Balance giữa realism và speed.

**CI Integration:** Integration test chạy trong CI. Slower than unit — chạy trên
commit hoặc PR. Parallel khi có thể. Fail fast. Clear error message khi fail.
"""  # noqa: E501

version = "0.0.1"
