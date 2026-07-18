title = "影像後製與標註流程"

content = """
- 匯入原始 DICOM 至工作站，檢查標籤完整性（PatientID、StudyDate、Modality）。
- 裁切多餘邊緣，保留解剖結構完整；使用標準窗寬/窗位（骨窗 W2000/L500、軟組織 W400/L40）。
- 標註：測量長度、角度、面積，單位統一為 mm、度、cm²。
- 加入病歷號、檢查日期、部位、技術員代碼水印，防止誤用。
- 輸出為 DICOM Secondary Capture 上傳 PACS，並備份至本地 NAS（保留 30 天）。
"""  # noqa: E501

version = "0.0.1"
