title = "API 테스트"

content = """
API 테스트는 REST, GraphQL 등 API 엔드포인트의 요청·응답을 검증합니다. UI보다 안정적이고 빠르며 자동화에 적합합니다.

**검증 대상**: 상태 코드, 응답 스키마, 필드 값, 에러 케이스(400, 401, 404 등)를 확인합니다.

**도구**: requests(Python), axios + Jest, Postman/Newman, pytest-httpx 등을 사용합니다. OpenAPI 스펙 기반으로 테스트를 생성할 수 있습니다.

**인증**: 토큰, API 키 등 인증 방식을 테스트 환경에 맞게 설정합니다. 시크릿은 환경 변수로 관리합니다.
"""  # noqa: E501

version = "0.0.1"
