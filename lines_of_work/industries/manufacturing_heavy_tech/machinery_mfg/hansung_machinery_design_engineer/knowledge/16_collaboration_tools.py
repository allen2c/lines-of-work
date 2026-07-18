title = "협업 툴 및 데이터 교환 표준"

content = """
- PDM: SolidWorks PDM Professional, 체크인/아웃, 워크플로 자동화(승인→릴리즈)
- PLM: Teamcenter 연계(EBOM↔MBOM 동기화, 변경 관리)
- 커뮤니케이션: Microsoft Teams 채널(프로젝트별), 일일 스탠드업 녹화 저장
- 일정 관리: Microsoft Project 온라인, 마일스톤 간트 차트 공유
- 파일 교환: 대용량 CAD 데이터는 전용 FTP(SSL) 또는 클라우드(OneDrive for Business) 사용
- 데이터 포맷: 네이티브(.sldprt/.sldasm) + 중립(STEP AP242, JT) 동시 제공
- 보안: 기밀 등급(Confidential) 태그 적용, 접근 권한 최소화, 로그 감사 월 1회
"""  # noqa: E501

version = "0.0.1"
