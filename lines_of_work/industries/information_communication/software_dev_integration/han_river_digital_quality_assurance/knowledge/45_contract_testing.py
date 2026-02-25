title = "계약 테스트"

content = """
계약 테스트는 API 제공자(Producer)와 소비자(Consumer) 간의 인터페이스 계약이 지켜지는지 검증합니다. 마이크로서비스 환경에서 유용합니다.

**Producer 테스트**: API가 선언된 스키마·계약을 따르는지 검증합니다.

**Consumer 테스트**: Consumer가 기대하는 요청·응답 형태를 Mock 서버로 제공하고, Consumer 테스트를 실행합니다.

**도구**: Pact가 대표적입니다. 계약 파일을 공유하여 양쪽이 동일한 계약을 따르는지 확인합니다.
"""  # noqa: E501

version = "0.0.1"
