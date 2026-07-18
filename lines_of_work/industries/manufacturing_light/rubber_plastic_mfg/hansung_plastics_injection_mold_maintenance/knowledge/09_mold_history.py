title = "금형 이력 관리 시스템"

content = """
- DB 스키마: mold_id, spec(캐비티, 재질), cumulative_shots, last_mount_date, repair_count, parts_replaced(json), inspection_log(array)
- 실시간 동기화: 장착/탈착 시 자동 업데이트(플러그인 API), 수리 완료 시 수동 승인 후 반영
- 조회 기능: 누적 샷 수 100만 단위 알림, 수리 횟수 5회 초과 시 교체 검토 플래그
- 백업: 일일 02:00 증분 백업, 월말 전체 백업 30일 보관
"""  # noqa: E501

version = "0.0.1"
