title = "Reviewing Customer Material and Process Specifications"

content = """
Customer orders often include specific material and process requirements that go beyond the basic part drawing. These requirements may be specified in separate material specifications, customer-specific quality clauses, industry standards, or notes on the purchase order. Failing to identify and comply with these requirements—even when the part dimensions are perfect—results in a nonconformance and possible rejection of the entire shipment.

**Sources of material and process requirements.**

1. **Drawing notes.** The most common location. Notes such as "MATERIAL: ASTM A108 GRADE 1018" or "ALL SURFACES SHALL BE SHOT PEENED PER SAE J441" are binding requirements.

2. **Customer purchase order clauses.** Customers frequently include quality flow-down clauses on their POs, such as: "Supplier shall maintain material traceability to mill certification" or "First article inspection required per AS9102." These clauses must be reviewed by QA before accepting the order.

3. **Referenced specifications.** Drawings may reference external documents: ASTM A36 (carbon steel), AMS 2750 (heat treatment requirements), ASME B46.1 (surface texture), or customer-proprietary specifications. All referenced documents must be available and current at Ridgecrest before production starts.

4. **Approved material substitution.** If the specified material is unavailable, a substitution requires written customer approval before any alternative material is used. "Similar" is not the same as "approved." Document the customer approval and attach it to the work order traveler.

**Common material specifications encountered at Ridgecrest.**
- ASTM A36: Hot-rolled structural steel. Most common general-purpose carbon steel.
- ASTM A108: Cold-drawn carbon steel bar. Tighter tolerance and better surface than A36.
- ASTM A240 / AISI 304, 316: Stainless steel sheet and plate.
- AMS 4027 / 6061-T6: Aluminum alloy.
- ASTM A513: DOM (drawn over mandrel) mechanical tubing.

**Process specifications.** Process requirements such as heat treatment (quench and temper to specific hardness range), plating (zinc, chrome, electroless nickel to defined thickness), passivation (per ASTM A967 for stainless), and weld qualification (per AWS D1.1) must be verified before the work order is released. Outside processing must be directed to an approved supplier on the Ridgecrest approved vendor list.

Whenever there is any doubt about what a material or process requirement means, the question goes to engineering or QA before production starts—not after a run is complete.
"""

version = "0.0.1"
