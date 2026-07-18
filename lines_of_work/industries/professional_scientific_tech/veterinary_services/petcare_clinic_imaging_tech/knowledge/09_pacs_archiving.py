title = "PACS 存檔與命名規範"

content = """
- 檔名格式：`YYYYMMDD_病歷號_部位_序號`，例 `20251215_A12345_CHEST_01`。
- Study Description 填寫：`Chest VD/DV`、`Abdomen Lateral`、`Cardiac Echo` 等標準術語。
- Series Number 依拍攝順序遞增，避免重複。
- 儲存策略：線上熱存 3 年，近線冷存 7 年，離線歸檔 10 年，符合《醫療資料保存年限規定》。
- 存取權限：技術員讀寫、獸醫師讀寫、行政唯讀，採角色基礎存取控制（RBAC）。
"""  # noqa: E501

version = "0.0.1"
