title = "스트리밍 플랫폼 사양"

content = """
Spotify, Apple Music, Tidal 등 스트리밍 서비스는 각각 권장 마스터 사양을 제시합니다.

**공통 요구사항**
- WAV 또는 FLAC(무손실)
- 44.1kHz 또는 48kHz, 16bit 또는 24bit
- -1dBFS 이하 True Peak(인터샘플 피크 고려)
- Loudness: 대부분 -14 LUFS(integrated) 기준

**플랫폼별 차이**
- Spotify: -14 LUFS, -1dBTP
- Apple Music: -16 ~ -1 LUFS 허용, -1dBTP
- Tidal: Hi-Res 지원, 96kHz/24bit 권장
- YouTube: -14 LUFS 권장

운영 담당자는 고객이 타깃하는 플랫폼에 맞는 사양을 안내하고, 마스터 출력 시 해당 사양 준수 여부를 검증합니다.
"""

version = "0.0.1"
