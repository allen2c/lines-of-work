title = "메타데이터 표준화(DDEX ERN 4.1)"

content = """
- 필수 요소: Resource(트랙), Release(앨범), Deal(배포 조건), Party(아티스트/레이블/프로듀서), Territory(국가 코드 ISO 3166-1 alpha-2).
- 한국어/영어 병기 필수: 아티스트명, 앨범 타이틀, 트랙 타이틀.
- 장르 매핑: 내부 장르 코드(예: KPOP=KPOP01) → DDEX GenreType(예: Pop) 변환 테이블 유지.
- 크레딧 역할 코드: 작곡(C), 작사(LA), 편곡(AR), 프로듀서(P), 세션 연주자(SM) 등 표준 코드 사용.
- 검증 스크립트(python ddex-validator) 실행, 오류 리포트 JSON으로 저장, 티켓에 첨부.
"""  # noqa: E501

version = "0.0.1"
