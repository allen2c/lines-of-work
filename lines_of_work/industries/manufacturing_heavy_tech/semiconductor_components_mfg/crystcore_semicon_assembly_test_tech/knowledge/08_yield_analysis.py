title = "良率分析與不良分類"

content = """
- 每小時由MES自動計算各站良率（Yield = 良品數 / 投入數 × 100%）。目標：Die Bond≥99.5%，Wire Bond≥99.0%，Molding≥98.5%，Saw≥99.0%，Test≥98.0%（含測試誤判）。
- 不良分類代碼（Defect Code）需統一使用公司標準，例如：DB01（Die Crack）、DB02（Die Shift）、WB01（NSOP）、WB02（Wire Sweep）、ML01（Void）、ML02（Flash）、SW01（Chipping）、TS01（Contact Fail）、TS02（Functional Fail）。
- 每班結束前需彙整不良分布，使用Pareto圖找出前三大不良項目，並在交接班會議中報告。
- 若某站良率連續2小時低於目標，需立即暫停該機台並進行原因調查（魚骨圖分析），同時通知領班與製程工程師。
"""  # noqa: E501

version = "0.0.1"
