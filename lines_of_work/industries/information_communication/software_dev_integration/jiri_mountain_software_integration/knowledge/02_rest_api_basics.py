title = "REST API 기초"

content = """
REST는 HTTP를 기반으로 한 아키텍처 스타일로, 리소스 중심의 API 설계를 지원합니다.
대부분의 시스템 통합에서 REST API가 기본 프로토콜로 사용됩니다.

**원칙:** 리소스는 URI로 식별됩니다. HTTP 메서드(GET, POST, PUT, PATCH, DELETE)로
작업을 표현합니다. stateless 통신을 유지하고, JSON 또는 XML로 데이터를 교환합니다.
캐시 가능한 응답은 적절한 헤더로 표시합니다.

**통합 시 고려사항:** 인증(API 키, OAuth, JWT) 방식을 확인합니다. 페이징, 정렬,
필터링 파라미터의 규칙을 파악합니다. rate limit와 오류 응답 형식을 문서화합니다.
재시도 가능한 메서드(GET, PUT, DELETE)와 그렇지 않은 메서드(POST)를 구분하여
멱등성 전략을 수립합니다.
"""  # noqa: E501

version = "0.0.1"
