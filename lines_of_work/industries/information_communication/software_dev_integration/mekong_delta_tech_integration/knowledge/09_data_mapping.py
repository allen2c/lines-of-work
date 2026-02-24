title = "Ánh xạ dữ liệu"

content = """
Data mapping chuyển đổi dữ liệu từ schema nguồn sang schema đích. Đòi hỏi hiểu rõ
cả hai bên và xử lý edge cases.

**Schema Alignment:** Document mapping rules rõ ràng. Field A nguồn → field B đích. Xử lý
nested objects và arrays. Có transformation logic (concatenate, split, lookup).

**Type Coercion:** Chuỗi sang số, date format conversion, timezone handling. Chuẩn hóa
format trước khi map. Validate output schema.

**Default and Fallback:** Khi thiếu giá trị nguồn, dùng default hoặc null theo business
rule. Log khi dùng fallback để audit. Có thể reject record nếu field bắt buộc thiếu.

**Mapping Tools:** Có thể dùng code (Python, Java), config-driven (JSON/YAML mapping),
hoặc visual ETL tool. Chọn theo complexity và maintainability.
"""  # noqa: E501

version = "0.0.1"
