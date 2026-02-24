title = "CSV Parsing"

content = """
CSV common cho data exchange. Parsing có edge cases. Integration với file-based.
Mekong Delta Tech parse CSV correctly.

**Encoding:** UTF-8. BOM handling. Vietnamese. Detect encoding. Validate.
Reject invalid. Document. Consistent. Test với Vietnamese data.

**Delimiter:** Comma default. Semicolon (locale). Tab. Quote. Escape. Configurable.
Header row. Detect. Document format. RFC 4180 khi possible.

**Edge Cases:** Quote trong field. Newline trong field. Empty field. Trailing
comma. Large file. Streaming. Memory. Robust parser. Handle malformed.
Error report. Don't fail entire.

**Validation:** Schema. Type. Range. After parse. Reject invalid row. Report.
Continue hoặc fail. Configurable. Data quality. Log.
"""  # noqa: E501

version = "0.0.1"
