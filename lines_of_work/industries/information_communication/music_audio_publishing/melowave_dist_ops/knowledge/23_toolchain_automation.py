title = "자동화 도구 체인 및 버전 관리"

content = """
- CI/CD: GitHub Actions → 빌드(파이썬 3.11), 테스트(pytest), 배포(ECS Fargate).
- 메타데이터 변환기: ddex-converter v2.3.1(내부 패키지), 세만틱 버저닝.
- 아트웍 처리: ImageMagick 7.1.1, FFmpeg 6.0.
- 정산 파이프라인: Airflow 2.7 DAGs, 매일 03:00 KST 실행.
- 모니터링: Prometheus + Grafana, 알림: Alertmanager → 슬랙/페이저듀티.
- 문서화: MkDocs(내부 위키), 변경 이력 CHANGELOG.md 관리.
"""  # noqa: E501

version = "0.0.1"
