title = "Bill of Materials (BOM): Reading and Using on the Floor"

content = """
A Bill of Materials (BOM) is the structured list of all components, raw materials, and sub-assemblies required to manufacture one unit of a finished product. On the shop floor at Ridgecrest Metalworks, the BOM drives what material is issued from the warehouse to each work order and defines the quantities used in production cost calculations.

**BOM structure.** A single-level BOM lists the direct components of a finished part. A multi-level (indented) BOM shows parent-child relationships across multiple assembly levels. For example, a fabricated steel bracket (Level 0) might require a laser-cut blank (Level 1), which in turn requires a specific sheet steel grade and gauge (Level 2). Understanding which level you are working at prevents confusion when issuing materials.

**Key BOM fields.**

- **Component material number:** The unique identifier for each required raw material or purchased component.
- **Description:** The human-readable material description.
- **Quantity per:** Amount of the component needed per one finished unit. May be expressed in pieces, kilograms, meters, liters, or other units of measure.
- **Unit of measure:** Must match the unit in which material is stored in inventory (e.g., if sheet steel is stored in kg, the BOM qty must be in kg, not in sheets).
- **BOM revision level:** The BOM has a revision history that must correspond to the current engineering drawing revision. Mismatches indicate a pending or missed ECO update.

**Using the BOM for material issuance.** When a warehouse associate picks components for a work order, they compare the quantity on the work order BOM component list against what they are physically picking. Over-issues waste material; under-issues cause production stops. Any discrepancy between the system BOM quantity and the physical material available is reported to the planner before the kit is sent to the floor.

**BOM accuracy and scrapping.** If scrap is generated during a run and additional material is needed, a supplemental material issue is posted to the work order. This extra material consumption vs. the BOM standard quantity becomes a material usage variance that is reviewed at order close.

**Floor BOM corrections.** If an operator notices that the BOM quantity does not match actual usage (e.g., a component is consistently left over or runs short every time), they must not independently adjust quantities. The discrepancy is reported to engineering on a BOM change request form for formal review and correction.
"""

version = "0.0.1"
