title = "Capacity Tickets – Power Capacity"

content = """
- When a power capacity request arrives, check the floor plan for the target rack location and its circuit breaker rating (e.g., 30A, 60A).
- Sum the existing load on that PDU (from BMS or PDU display) and add the requested load. Ensure total ≤ 80% of breaker rating.
- If the request exceeds 80%, suggest an alternative rack or PDU with available capacity. Document the calculation.
- Update the capacity database with the new allocation. Attach the ticket to the rack asset record.
- For three‑phase PDUs, balance phases within 10% of each other. If imbalance > 10%, flag for rebalancing.
"""

version = "0.0.1"
