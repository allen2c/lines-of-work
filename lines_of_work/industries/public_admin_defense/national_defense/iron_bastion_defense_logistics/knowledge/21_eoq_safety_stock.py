title = "EOQ and Safety Stock Calculations"

content = """
Economic Order Quantity (EOQ) and safety stock are foundational inventory formulas used
to balance ordering cost, holding cost, and service level.

**EOQ:** EOQ minimizes total cost (ordering + holding) when demand and lead time are
stable. Formula: sqrt(2 * annual demand * order cost / holding cost per unit per year).
Use when the assumptions hold; otherwise use heuristics or simulation.

**Safety Stock:** Safety stock buffers against demand and lead time variability. Higher
variability or higher service targets require more safety stock. Formula depends on
demand distribution—often uses standard deviation and service factor (Z).

**Combined Use:** Reorder point = (average demand * lead time) + safety stock. Order
quantity can be EOQ or a fixed quantity. When stock hits reorder point, place order.

**Limitations:** These models assume continuous review. For periodic review systems,
adjust formulas accordingly. Real-world factors (minimum order quantities, shelf life)
may override pure economic logic.
"""  # noqa: E501

version = "0.0.1"
