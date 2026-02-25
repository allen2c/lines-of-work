title = "Material Tracking with Barcodes and RFID"

content = """
Ridgecrest Metalworks uses a combination of barcode scanning and, in select high-value material streams, RFID tracking to maintain real-time visibility of material location and status throughout the facility. These systems feed directly into the SAP ERP, eliminating manual data entry errors and providing audit-ready traceability records.

**Barcode system.** Every material lot receives a printed label with a Code 128 or QR barcode at receiving. The barcode encodes the material number, lot/heat number, storage location, quantity, and receipt date. Scanners are mounted at receiving, each production cell, the inspection station, and the shipping dock. Operators scan the material barcode and the work order barcode at each step to record the transaction.

**Label standards.** Labels must be printed on durable, oil-resistant stock. Heat-exposed areas (near furnaces or weld stations) require high-temperature label material. Labels must be affixed to the material or its container—not to the surrounding rack. If a label is damaged or falls off, the material is treated as unidentified until a new label is generated through the ERP and verified against physical identity by the supervisor or QA.

**Scan discipline.** Scanning at the point of activity—not at the end of the shift—is mandatory. Batch scanning causes inventory location errors and defeats the purpose of real-time tracking. If a scanner is unavailable, the transaction must be queued in writing on the paper backup log and entered as soon as a scanner is restored.

**RFID applications.** RFID passive tags are currently used on high-value heat-treated alloy coils and titanium stock. Fixed RFID readers at zone entry/exit points log material movement automatically as the load passes through, creating an automatic trail without any operator action. RFID data is reconciled with ERP inventory nightly; discrepancies trigger an alert to the inventory controller.

**Traveler scanning.** Shop traveler documents for each work order carry a barcode matching the work order number. At each operation, the operator scans the traveler barcode to record operation start and completion times. This data feeds OEE and on-time delivery metrics.

**Common problems.** Dirty scanner windows cause scan failures—clean the scanner face at the start of every shift. Bent or damaged labels may need to be reprinted. If a barcode will not scan after three attempts, contact the inventory controller rather than entering a manual transaction without supervisor approval.
"""

version = "0.0.1"
