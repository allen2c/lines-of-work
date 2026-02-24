title = "Xử lý Timezone"

content = """
DateTime handling dễ sai. Timezone, DST, storage format. Integration cần consistent
approach. Mekong Delta Tech use UTC internally, convert at edge.

**Storage:** Store UTC. ISO 8601 format với Z hoặc +00:00. Millisecond precision.
Never store local time without timezone. Migration cho existing wrong data.

**API:** Accept ISO 8601. With timezone (preferred) hoặc assume UTC nếu không có.
Return ISO 8601 UTC. Document format. Client convert to local for display.

**Vietnamese Context:** Vietnam UTC+7, no DST. Simplify. Still store UTC. Convert
+7 cho display. Business hour calculation. Document timezone assumption trong
API spec. Test với various timezone.
"""  # noqa: E501

version = "0.0.1"
