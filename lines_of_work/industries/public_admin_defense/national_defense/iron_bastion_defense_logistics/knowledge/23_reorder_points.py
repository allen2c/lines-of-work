title = "Reorder Points and Trigger Mechanisms"

content = """
Reorder points trigger replenishment when inventory falls to a defined level. Proper
setting balances responsiveness and cost.

**Calculation:** Reorder point = (average daily demand * lead time in days) + safety
stock. Accounts for consumption during the order lead time and buffers for variability.

**Lead Time:** Use realistic lead time—from order placement to receipt. Include
vendor processing, transit, and receiving. Update when lead times change.

**Trigger Mechanisms:** Continuous review systems check inventory after every
transaction. Periodic review systems check at fixed intervals. Choose based on
transaction volume and system capability.

**Minimum Order Quantities:** When minimum order quantity exceeds one cycle's demand,
reorder point may be higher to avoid frequent small orders. Balance against holding
cost and storage capacity.
"""  # noqa: E501

version = "0.0.1"
