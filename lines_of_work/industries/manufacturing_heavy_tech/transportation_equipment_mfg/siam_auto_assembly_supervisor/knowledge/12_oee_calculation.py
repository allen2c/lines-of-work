title = "การคำนวณ OEE (Overall Equipment Effectiveness)"

content = """
- OEE = Availability × Performance × Quality
- Availability = (เวลาทำงานตามแผน - Downtime) / เวลาทำงานตามแผน (เป้าหมาย ≥ 90%)
- Performance = (จำนวนคันที่ผลิตจริง × Takt) / เวลาทำงานจริง (เป้าหมาย ≥ 85%)
- Quality = (จำนวนคันดี / จำนวนคันที่ผลิตทั้งหมด) × 100 (เป้าหมาย ≥ 99.5%)
- คำนวณ OEE ทุกกะโดยใช้ระบบ MES และรายงานใน Dashboard
- หาก OEE ต่ำกว่า 75% ให้ดำเนินการ Root Cause Analysis ภายใน 24 ชั่วโมง
"""

version = "0.0.1"
