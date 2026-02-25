title = "Contract Testing"

content = """
Contract testing verify compatibility giữa consumer và provider mà không cần deploy
cả hai cùng lúc. Quan trọng cho microservices và integration.

**Consumer-Driven Contract:** Consumer định nghĩa expectation (request/response).
Provider test chống contract. Đảm bảo provider không break consumer. Pact là tool
phổ biến.

**Provider Verification:** Provider chạy mock request từ contract, verify response
match. Trong CI. Fail build khi contract break. Consumer và provider repo có thể
khác — share contract (file, broker).

**Contract as Documentation:** Contract thay thế hoặc bổ sung API doc. Always up-to-date
vì từ code. Generate doc từ contract khi có thể.

**Limitations:** Contract test không thay integration test end-to-end. Không catch
network, deployment, environment issues. Dùng kết hợp với integration test.
"""  # noqa: E501

version = "0.0.1"
