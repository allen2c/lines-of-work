title = "Pallet Putaway Strategies (FIFO/FEFO)"

content = """
- For perishable items (dairy, meat, produce), use FIFO (First In, First Out) based on receipt date. For items with explicit expiration dates (pharmaceuticals, prepared meals), use FEFO (First Expired, First Out).
- In the WMS, scan pallet barcode and select location. Ensure location is within the correct temperature zone and has capacity (max 2 pallets high for freezer, 3 for cooler).
- If a location is full, use the next available location in the same zone. Do not mix different SKUs on the same pallet.
- After putaway, update inventory count immediately. Conduct random spot checks on 5% of putaway pallets per shift.
"""  # noqa: E501

version = "0.0.1"
