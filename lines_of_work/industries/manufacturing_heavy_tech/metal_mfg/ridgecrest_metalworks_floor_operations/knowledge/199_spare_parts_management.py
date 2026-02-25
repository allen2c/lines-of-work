title = "Spare Parts Inventory and Critical Spares Policy"

content = """
Spare parts management at Ridgecrest Metalworks ensures that the right parts are available when maintenance is needed, minimizing equipment downtime without excessive inventory investment. Effective spare parts management balances the cost of holding inventory against the production loss cost of waiting for parts.

Parts are classified by criticality:

Critical spares (A-class): Parts whose absence would cause extended production downtime on critical equipment, and where procurement lead time is long (days to weeks). Examples: main spindle bearings for CNC machining centers, servo drives, PLC modules, hydraulic pump cartridges, and long-lead motor windings. These parts are held on-site at a defined minimum stock level regardless of consumption. The minimum stock level is set by the maintenance engineer based on lead time, failure frequency, and production impact.

Important spares (B-class): Parts needed regularly in maintenance with moderate lead time. Examples: standard bearing sizes, seal kits, filter elements, belts, and contactors. These are managed with min/max reorder levels in the CMMS; when stock falls to the reorder point, a purchase order is generated automatically.

Routine consumables (C-class): High-consumption, short lead-time items. Examples: lubricants, abrasive paper, cable ties, and standard fasteners. These are managed with a blanket purchase agreement and replenished on a regular schedule.

Spare parts storage: Parts are stored in a controlled storeroom organized by equipment or part category. Bearings are stored in their original packaging (away from vibration and electromagnetic fields, which cause false brinelling and demagnetization). Rubber seals are stored at ambient temperature away from UV, ozone, and solvents. Electrical components are stored in ESD-safe packaging where required. Parts are identified with their asset association (which machine they support) to prevent use of a critical spare on a non-critical machine.

Parts traceability: Critical spare parts (bearings, seals, and electronic components for safety systems) must have traceable origin — no counterfeit parts. Parts are sourced from authorized distributors; incoming parts are checked for correct part number and original manufacturer packaging.

Surplus and obsolete parts review: Annually, the spare parts inventory is reviewed. Surplus parts (held in excess of calculated maximum) and obsolete parts (for decommissioned equipment) are dispositioned: returned to the supplier, sold, or scrapped. This prevents the store becoming clogged with unusable inventory.
"""

version = "0.0.1"
