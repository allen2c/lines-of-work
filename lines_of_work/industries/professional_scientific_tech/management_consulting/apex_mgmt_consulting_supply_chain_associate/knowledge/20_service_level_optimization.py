title = "Service Level Optimization"

content = """
- Service level types: Cycle Service Level (CSL) = probability of no stockout per replenishment cycle; Fill Rate (FR) = fraction of demand satisfied from stock. CSL is easier to compute; FR is more customer-focused.
- Trade-off: higher service level requires more safety stock. Example: increasing CSL from 95% to 99% (z from 1.65 to 2.33) increases safety stock by 41% (2.33/1.65 -1).
- Use cost trade-off: stockout cost (lost sales, penalty) vs inventory holding cost. Optimal CSL = 1 - (holding cost per unit per year / stockout cost per unit). Example: holding cost $5, stockout cost $50 → optimal CSL = 1 - (5/50) = 0.9 (90%).
- For A items, target 99% fill rate; B items 95%; C items 90%. Monitor actual fill rate monthly.
"""  # noqa: E501

version = "0.0.1"
