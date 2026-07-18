title = "웹 애플리케이션 보안"

content = """
- OWASP Top 10 2021 기준: 취약한 접근 통제, 암호화 실패, 인젝션, 안전하지 않은 설계, 보안 설정 오류 등.
- SQL 인젝션: Prepared Statement 사용, 입력 값 검증, 에러 메시지 노출 금지.
- XSS(Cross-Site Scripting): 출력 인코딩, Content-Security-Policy 헤더, HttpOnly 쿠키.
- CSRF(Cross-Site Request Forgery): CSRF 토큰, SameSite 쿠키 속성, 중요 작업 재인증.
- 세션 관리: 세션 ID 예측 불가능, HttpOnly+Secure+SameSite, 세션 타임아웃(15분), 로그아웃 시 세션 파기.
"""  # noqa: E501

version = "0.0.1"
