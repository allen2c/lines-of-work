title = "代理檔案工作流程"

content = """
- 使用DaVinci Resolve或Premiere Pro產生代理檔案，格式優先選擇ProRes Proxy（Mac）或DNxHR LB（Windows）。
- 解析度設定為原始解析度的一半（例如4K素材產生1920x1080代理），幀率與原始一致。
- 代理檔案存放於專案資料夾內的「02_Proxy」子資料夾，命名規則：原始檔名加上「_proxy」後綴。
- 剪輯完成後，必須重新連結原始檔案（Relink）才能進行線上套片與調光。
- 重新連結後，使用「Compare」功能檢查是否有離線片段或連結錯誤。
"""

version = "0.0.1"
