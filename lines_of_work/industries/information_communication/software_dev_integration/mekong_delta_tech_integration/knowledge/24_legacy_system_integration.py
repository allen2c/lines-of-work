title = "Tích hợp hệ thống Legacy"

content = """
Legacy system thường thiếu API chuẩn, documentation, hoặc công nghệ hiện đại.
Tích hợp đòi hỏi creativity và careful design. Phổ biến tại Vietnam market.

**Assessment:** Hiểu data format, protocol (SOAP, FTP, file-based), availability.
Có mainframe, COBOL, hoặc closed proprietary system. Document as-is architecture.

**Adapter Pattern:** Tạo adapter layer giữa legacy và modern system. Adapter translate
protocol, format, semantics. Isolate legacy complexity. Adapter có thể là ETL job,
message translator, hoặc API gateway.

**Incremental Migration:** Không big-bang. Strangler fig pattern — route traffic
dần sang system mới. Dual-write during transition. Feature flag. Rollback plan.

**Data Quality:** Legacy data thường có quality issue. Validation, cleansing,
deduplication. Handle encoding (EBCDIC, legacy charset). Document data lineage.
"""  # noqa: E501

version = "0.0.1"
