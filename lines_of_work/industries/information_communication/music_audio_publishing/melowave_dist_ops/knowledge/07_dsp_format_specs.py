title = "DSP별 기술 사양 준수"

content = """
- 오디오: 44.1kHz/16bit WAV(멜론, 지니), 48kHz/24bit FLAC(스포티파이, 애플), 44.1kHz/16bit MP3 320kbps(유튜브뮤직).
- 메타데이터: DDEX ERN 4.1 전 DSP 공통, 단 애플뮤직은 iTunes Package(iTunesMetadata.plist) 추가.
- 아트웍: 스포티파이 640×640px 별도 썸네일 생성, 애플 3000×3000px 원본 사용.
- 지역 제한: 한국 전용 발매 시 Territory=KR만 포함, 글로벌 발매 시 Worldwide(단, 권리 미확보 국가 제외).
- DRM: 멜론/지니 DRM 적용 필수, 글로벌 DSP는 DRM 미적용.
"""  # noqa: E501

version = "0.0.1"
