title = "OAuth와 인증"

content = """
OAuth 2.0은 위임 인증의 표준 프로토콜로, 클라이언트가 사용자 권한 없이 리소스에
접근할 수 있게 합니다. API 통합에서 서비스 간 인증에 널리 쓰입니다.

**그랜트 타입:** Authorization Code(웹앱), Client Credentials(서비스 간), Refresh
Token(세션 갱신)을 시나리오에 맞게 선택합니다. 암시적(Implicit) 그랜트는 보안상
비권장입니다.

**구현 시 주의:** Client secret은 안전하게 보관하고 코드에 하드코딩하지 않습니다.
리다이렉트 URI를 화이트리스트로 제한합니다. 토큰 만료 시간을 적절히 설정하고 갱신
로직을 구현합니다. PKCE를 지원하는 경우 모바일·SPA에서 권장합니다.
"""  # noqa: E501

version = "0.0.1"
