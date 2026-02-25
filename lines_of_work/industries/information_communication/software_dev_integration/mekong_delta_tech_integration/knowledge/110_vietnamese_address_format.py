title = "Định dạng địa chỉ Việt Nam"

content = """
Địa chỉ Việt Nam có structure: số nhà, đường, phường/xã, quận/huyện, tỉnh/thành.
Integration validate, store, display. Mekong Delta Tech handle address format.

**Structure:** Hierarchical. Tỉnh/Thành phố > Quận/Huyện > Phường/Xã > Đường >
Số nhà. Optional fields. Variation. No strict standard. Flexible. Validate
per level. Lookup table cho admin division.

**Validation:** Required level. Format. Length. No injection. Normalize.
Unicode. Vietnamese character. Store structured (fields) hoặc free text.
Search. Geocoding. Document. API accept format. Partner format? Map.

**Integration:** Address từ partner. Validate. Normalize. Store. Display.
Shipping. Compliance. PDPA. Don't over-validate — accept variation. Improve
over time.
"""  # noqa: E501

version = "0.0.1"
