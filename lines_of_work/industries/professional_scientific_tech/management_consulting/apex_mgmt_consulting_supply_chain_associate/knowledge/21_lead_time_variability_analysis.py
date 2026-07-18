title = "Lead Time Variability Analysis"

content = """
- Measure lead time from supplier: collect data on order-to-delivery time for at least 30 orders. Calculate mean (L) and standard deviation (σ_L).
- Impact on safety stock: if both demand and lead time vary, use formula SS = z * sqrt( (σ_d^2 * L) + (d^2 * σ_L^2) ). Example: d=100, σ_d=20, L=10, σ_L=2, z=1.65 → SS = 1.65 * sqrt( (400*10) + (10000*4) ) = 1.65 * sqrt(4000+40000) = 1.65 * sqrt(44000) ≈ 1.65*209.8 ≈ 346 units.
- If lead time variability is high (σ_L > 0.5*L), consider supplier improvement or dual sourcing. Track lead time performance monthly; if σ_L increases by >20%, recalculate safety stock.
"""  # noqa: E501

version = "0.0.1"
