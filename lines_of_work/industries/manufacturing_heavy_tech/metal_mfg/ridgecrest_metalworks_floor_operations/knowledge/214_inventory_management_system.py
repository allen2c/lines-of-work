title = "ERP Inventory Management: Transactions and Accuracy"

content = """
Ridgecrest Metalworks uses an ERP system (currently SAP S/4HANA) to manage all inventory transactions across the facility. Accurate real-time inventory data is critical for production scheduling, purchasing decisions, and financial reporting. Every operator who touches material has a role in maintaining that accuracy.

**Key transaction types floor personnel execute:**

- **Goods Receipt (GR):** Posted when material is received from a supplier against a PO. The receiving team posts GR after incoming inspection is complete, not before.
- **Goods Issue (GI):** Posted when raw material is issued to a production work order. This reduces raw material stock and adds cost to the order. GI must happen at the time of actual material issue, not at end of shift.
- **Transfer Order / Stock Transfer:** Posted when material moves between storage locations within the facility (e.g., from raw material Zone B to WIP Zone D).
- **Production Confirmation:** Posted at each routing step as work is completed, recording labor hours and moving the order to the next operation.
- **Goods Receipt from Production:** Posted when finished parts are moved from the last production step to finished goods.
- **Return to Stock:** Unused material returned from a work order is posted back to raw material inventory with the original lot and heat number preserved.

**Accuracy standards.** Inventory accuracy target is 98% or higher by location and quantity, measured monthly during cycle counts. Accuracy below 95% for any material class triggers a root-cause investigation.

**Common errors to avoid.** Posting a transaction to the wrong work order or storage location is the leading cause of phantom inventory (system shows stock but stock is not physically there). Operators must confirm the work order number and material number on the screen before confirming any transaction. Scanning barcodes is mandatory where labels are present—manual entry is a last resort.

**Negative inventory.** A negative inventory balance (system shows quantity below zero) indicates a missing GR or GI posting error. Negative balances must be reported to the warehouse supervisor immediately—they cannot be ignored because they corrupt production cost calculations and MRP signals.

System access is role-based. Operators have transaction rights specific to their area. Any request to access another user's credentials must be refused and reported to IT.
"""

version = "0.0.1"
