title = "Production Sequence Planning from Drawing to Shipment"

content = """
Production sequence planning is the process of determining the optimal order of manufacturing operations to transform raw material into a finished part that meets all drawing requirements, in the most efficient manner, with the earliest possible delivery. At Ridgecrest Metalworks, the manufacturing engineer creates the routing during new part launch, and the production planner schedules work orders against that routing.

**General sequencing principles.**

1. **Hold features late.** Precision features (tight-tolerance bores, critical surfaces, threaded features) should be machined as late in the sequence as possible to minimize the risk of damage or distortion from subsequent operations. A precision bore machined early can be damaged by the heat of welding that follows.

2. **Remove distortion before finishing.** Welded fabrications distort. If a part requires post-weld machined surfaces, stress relief or straightening must occur between welding and final machining to ensure the part meets geometric tolerances.

3. **Surface treatment last.** Plating, anodizing, painting, and coating are almost always the last operation before final inspection and packaging. These surfaces are easily damaged and must not be exposed to subsequent metalworking operations.

4. **Inspection gates at critical transitions.** Inspection checkpoints in the routing are placed after operations where defects, if undetected, would cause significant downstream cost. For example: inspect first-piece after the first machining operation before committing the full batch to subsequent operations.

5. **Outside processing.** Operations performed by subcontractors (heat treatment, plating, special NDT) are inserted into the routing at the correct sequence and managed as outside processing purchase orders linked to the main work order.

**Example sequence for a machined steel bracket.**
- Op 10: Laser cut blank from sheet (material: A36, 6 mm)
- Op 20: First-piece inspection and traveler check
- Op 30: Press brake form to print
- Op 40: MIG weld reinforcement tabs per drawing
- Op 50: Grind weld flush per drawing note
- Op 60: CNC mill mounting holes and slots to tolerance
- Op 70: Final inspection (all dimensions, surface finish)
- Op 80: Apply rust inhibitor oil; pack and ship

**Routing changes.** Any change to the approved routing after the part is in production must be authorized through the ECO or concession process. A supervisor who reroutes parts through an unlisted operation to meet schedule creates a traceability gap and a potential quality nonconformance.
"""

version = "0.0.1"
