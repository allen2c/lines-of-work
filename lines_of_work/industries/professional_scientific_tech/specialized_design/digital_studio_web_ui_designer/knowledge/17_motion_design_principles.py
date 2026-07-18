title = "動態設計原則"

content = """
- 動畫持續時間：微互動100-200ms，頁面轉場300-400ms，載入動畫不超過1秒。
- 緩動函數：進出使用ease-in-out，強調使用ease-out，警告使用ease-in。
- 避免同時觸發多個動畫，造成視覺混亂。
- 所有動畫需有減少動畫模式（prefers-reduced-motion），使用CSS media query。
- 動畫規格需以Lottie或CSS關鍵影格提供，並標示觸發條件。
"""  # noqa: E501

version = "0.0.1"
