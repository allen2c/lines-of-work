title = "Inventory Policy Types"

content = """
- Continuous review (Q,R): order fixed quantity Q when inventory reaches reorder point R. Suitable for high-volume, stable demand.
- Periodic review (T,S): order up to target level S every review period T. Good for items with many SKUs or coordinated ordering.
- EOQ (Economic Order Quantity): EOQ = sqrt(2DS/H) where D = annual demand, S = order cost, H = holding cost per unit per year. Example: D=10,000, S=$50, H=$5 → EOQ=447 units.
- Safety stock: SS = z * σ_d * sqrt(L) for demand variability only; add lead time variability term if needed. Service level targets: A items 95%, B items 85%, C items 70%.
"""  # noqa: E501

version = "0.0.1"
