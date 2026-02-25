title = "Warehouse Layout, Slotting, and Rack Management"

content = """
The Ridgecrest Metalworks warehouse and raw material storage areas are organized to maximize space utilization, minimize travel distance, and maintain clear separation between material types, grades, and statuses. A well-slotted facility reduces pick times, prevents grade mix-ups, and makes cycle counting accurate.

**Zone definitions.** The facility is divided into labeled zones:
- Zone A: Raw material incoming and hold
- Zone B: Steel coil and sheet storage (heavy rack and floor stack)
- Zone C: Bar stock, tube, and structural shapes (cantilever racks)
- Zone D: WIP (work-in-process) staging between operations
- Zone E: Finished goods and pre-shipment staging
- Zone F: Consumables and packaging supplies

Each zone is painted and signposted at floor level and overhead. Zones must not be used interchangeably without a formal layout change approved by the warehouse supervisor.

**Rack types.** Pallet racks hold steel sheet and plate bundles with appropriate beam capacities. Cantilever racks are designed specifically for long bar stock, extrusions, and tube—horizontal arms at varying heights hold each tier. Coil cradles on the floor store sheet steel coils vertically (eye to the sky) or horizontally depending on coil weight and crane access requirements.

**Slotting logic.** High-turn materials are slotted nearest to the production entry point to reduce travel. Low-turn or specialty alloys are in deeper positions. Similar grades are never stored adjacent without a visual separator or label barrier—co-mingling A36 and 4140 alloy bar stock in the same rack section, for example, creates undetectable mix risk.

**Weight limits.** Every rack section has a posted maximum load rating. Rack load ratings must not be exceeded. Rack inspection is performed quarterly; any bent upright, damaged beam, or missing safety pin must be tagged out immediately.

**Location coding.** Each rack bay and level has a unique address (e.g., B-03-C-2 = Zone B, Bay 3, Column C, Level 2). ERP inventory records reference these location codes. When material is moved, both the source and destination locations must be updated in the system before the operator leaves the area.

Floor stacks must have stable base dunnage, must not exceed stable height-to-base ratios, and must be clearly labeled with the same information required on rack slots.
"""

version = "0.0.1"
