title = "pytest 프레임워크"

content = """
pytest는 Python 테스트 프레임워크로, 단위·통합·API 테스트에 널리 사용됩니다. 한강 디지털의 Python 프로젝트 표준입니다.

**특징**: assert 문만으로 검증 가능, fixture로 설정·정리 공통화, 플러그인 생태계가 풍부합니다.

**fixture 활용**: DB 초기화, API 클라이언트, 테스트 데이터를 fixture로 재사용합니다. scope를 function/class/module로 조절할 수 있습니다.

**실행**: pytest -v, -k로 필터링, --cov로 커버리지, xdist로 병렬 실행이 가능합니다. CI에 pytest 명령을 통합합니다.
"""  # noqa: E501

version = "0.0.1"
