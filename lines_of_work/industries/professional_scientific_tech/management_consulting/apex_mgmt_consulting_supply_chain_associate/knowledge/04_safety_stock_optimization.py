title = "Safety Stock Optimization"

content = """
- Factors: demand variability (σ_d), lead time variability (σ_L), desired service level (z-score). For both variable: SS = z * sqrt( (σ_d^2 * L) + (d^2 * σ_L^2) ) where d = average demand per period.
- Example: daily demand mean=100, σ_d=20, lead time mean=5 days, σ_L=1 day, service level 95% (z=1.65). SS = 1.65 * sqrt( (20^2*5) + (100^2*1^2) ) = 1.65 * sqrt(2000+10000) = 1.65 * sqrt(12000) ≈ 1.65*109.5 ≈ 181 units.
- Review frequency: recalculate safety stock quarterly or when demand/lead time patterns change significantly (>20% shift in mean or variance).
"""  # noqa: E501

version = "0.0.1"
