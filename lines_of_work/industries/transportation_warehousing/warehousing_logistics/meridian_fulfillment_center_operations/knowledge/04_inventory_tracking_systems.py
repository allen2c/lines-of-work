title = "Inventory Tracking and WMS Fundamentals"

content = """
Meridian Fulfillment Center relies on a Warehouse Management System (WMS) to
maintain real-time visibility of every inventory unit within the facility.
Accurate tracking is essential for order fulfillment and inventory control.

**License Plate Numbers (LPN):** Each pallet, carton, or totes receives a unique
LPN barcode that identifies its contents. The LPN serves as the tracking handle
throughout warehouse operations. Scanning the LPN retrieves the complete content
detail without requiring individual unit scans.

**Stock Keeping Units (SKU):** Every distinct product is assigned a unique SKU
that encodes product attributes like size, color, and style. The SKU is the
fundamental unit of inventory management, enabling precise tracking of
individual items within larger containers.

**Location Barcodes:** Every storage location carries a unique barcode
identifying the aisle, bay, level, and position. Location scans during putaway,
picking, and cycle counting confirm that inventory is where the system expects it
to be. Mis-scans or missed scans create inventory discrepancies.

**Transaction Types:** The WMS records every inventory movement with a
transaction code. Receipts, putaways, picks, replenishments, cycle counts, and
adjustments all generate audit trails. This history enables traceability and
supports inventory reconciliation.

**Real-Time Updates:** Scan transactions update inventory status immediately,
making stock available for allocation or marking it as committed to orders.
Batch updates are avoided as they create visibility gaps during processing
delays. Real-time accuracy supports the 99.5% inventory accuracy target.
"""

version = "0.0.1"
