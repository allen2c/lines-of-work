"""Incrementality testing for causal measurement."""

title = "증분성 테스트"

content = """
광고가 실제로 전환을 발생시켰는지, 없었어도 발생했을 전환인지 구분하는 인과 추론 방법이다.

**방법:** 홀드아웃(Geo, 사용자), PSA(Public Service Announcement) 대조군 등. 테스트군에만
광고를 노출하고 대조군과 전환 차이를 비교한다. 통계적 유의성과 MDE(Minimum Detectable Effect)를
사전에 설계한다.

**적용:** 신규 채널 도입, 예산 증액, 크리에이티브 변경 시 증분 효과 검증에 활용한다. 플랫폼
내장 도구(메타 Conversion Lift, 구글 Geo Experiments) 또는 서드파티 솔루션을 사용한다.

**한강디지털 기준:** 주요 전략 변경 시 증분성 테스트를 제안하고, 결과를 캠페인 최적화에 반영한다.
"""  # noqa: E501

version = "0.0.1"
