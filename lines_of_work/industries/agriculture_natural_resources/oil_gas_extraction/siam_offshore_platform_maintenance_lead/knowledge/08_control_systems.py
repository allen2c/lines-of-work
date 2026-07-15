title = "ระบบควบคุม"

content = """
- ระบบ DCS (Distributed Control System) ของ Yokogawa Centum VP ควบคุมกระบวนการผลิตทั้งหมด
- PLC สำหรับระบบความปลอดภัย (SIL 2/3) ตรวจสอบการทำงานของ logic solver ทุก 3 เดือน
- SCADA สำหรับตรวจสอบระยะไกล ต้องทดสอบการสื่อสารกับฝั่งทุกวัน
- ระบบ alarm management: กำหนด priority สูง/กลาง/ต่ำ ตรวจสอบ alarm flood ทุกเดือน
- การสำรองข้อมูล (backup) ของ configuration file ทุกสัปดาห์ และหลังการเปลี่ยนแปลงทุกครั้ง
"""

version = "0.0.1"
