title = "Định dạng số tiếng Việt"

content = """
Số, tiền tệ có format địa phương. Việt Nam: dấu phân cách khác. Integration
hiển thị, parse. Mekong Delta Tech handle Vietnamese format.

**Number:** 1.234.567,89 (dot thousand, comma decimal) vs US 1,234,567.89.
Locale. Parsing: detect, convert. Storage: standard format (no separator).
Display: format per locale. i18n. Library (Intl). Don't assume.

**Currency:** VND. Symbol ₫. No decimal (đồng). Format. API: amount in minor
unit (VND no decimal) hoặc decimal. Document. Consistent. Partner format?
Convert. Validate.

**Integration:** Accept multiple format? Or standard only. Document. Validate.
Convert at boundary. Internal standard. Display convert. Test. Vietnamese
locale. Edge case. QA.
"""  # noqa: E501

version = "0.0.1"
