title = "Capacity Tickets – Cooling Capacity"

content = """
- Each row has a cooling capacity in kW (e.g., 50 kW per row). Check current cooling load from BMS (sum of CRAC unit capacities minus reserve).
- For a new equipment request, estimate heat output (typically 80% of nameplate power draw). Add to row cooling load.
- If total cooling load exceeds 80% of row capacity, flag for facilities to consider adding portable cooling or redistributing load.
- Ensure the equipment is placed in a row with adequate cooling – avoid placing high‑density gear in a row already near capacity.
- Document the cooling allocation in the capacity ticket and update the row cooling budget.
"""

version = "0.0.1"
