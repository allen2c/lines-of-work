title = "보안 이벤트·사이버 위협 대응"

content = """
- 보안 관제(SoC)와 NOC의 협업: NOC는 망 가용성·성능, SoC는 보안 위협·침해로 역할을 분리하되, DDoS·랜섬웨어 등 망·보안 동시 영향 이벤트는 합동 대응.
- DDoS 공격 징후: 트래픽 평소 대비 3배 이상 1분, 동일 src ASN·동일 dst port 집중, BGP Flowspec·RTBH(Remotely Triggered Black Hole) 자동 적용.
- DNS·NTP·SSDP·memcached 등 Reflection 공격은 상류 ISP와 협력 트래픽 차단, L7 공격은 CDN·WAF에서 흡수, 공격 종료 후 정책 정리.
- 계정·권한 관리: NOC 콘솔·네트워크 장비 접근은 PKI + 일회용 OTP(예: Duo, Yubikey), 권한 분기 90일 재인증, 비번 90일 변경.
- 보안 사고: 정보통신망법 §28의 "정보통신망 침해사고"에 해당 시 1시간 내 과기정통부 신고, 24시간 내 2차 보고, 한국인터넷진흥원(KISA) 합동 조사 협력.
"""  # noqa: E501

version = "0.0.1"
