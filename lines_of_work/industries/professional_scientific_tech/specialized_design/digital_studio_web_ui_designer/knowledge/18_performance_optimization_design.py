title = "設計效能優化"

content = """
- 圖片壓縮：使用WebP格式，品質80%，最大尺寸不超過2000px寬。
- 減少HTTP請求：合併小圖示為Sprite，使用SVG符號。
- 字型載入：使用font-display:swap，僅載入所需字重（如Regular、Bold、Medium）。
- 避免過多陰影與漸層，減少GPU渲染負擔。
- 設計稿中標示可延遲載入的區塊（如折疊區以下內容）。
"""  # noqa: E501

version = "0.0.1"
