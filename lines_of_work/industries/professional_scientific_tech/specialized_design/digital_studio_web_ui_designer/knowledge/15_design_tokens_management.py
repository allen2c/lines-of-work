title = "設計Token管理"

content = """
- 定義Token層級：Global（全域值，如顏色#FF0000）、Alias（語意別名，如color-primary）、Component（元件專用，如button-bg）。
- 使用JSON或YAML格式儲存Token，並與前端工程師共享（如Style Dictionary）。
- Token命名規則：類別-屬性-狀態（如color-background-primary-hover）。
- 每次更新Token需同步更新設計系統與前端程式碼，避免不一致。
- 定期審查Token使用率，移除未使用的Token。
"""  # noqa: E501

version = "0.0.1"
