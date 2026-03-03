title = "Replenishment Strategies"

content = """
Replenishment restocks picking locations
from reserve. Effective strategies
ensure availability without excess
at Indus Bazaar.

**Min-Max:** Replenish when inventory
falls below minimum to maximum level.
Simple. May cause stockouts if demand
spikes. Adjust parameters based on
turnover and variability.

**Reorder Point:** Trigger when
inventory reaches reorder point.
Order quantity may be fixed or
variable. Account for lead time
and safety stock. Common for
purchasing; adapt for internal
replenishment.

**Wave Replenishment:** Replenish
before picking waves. Ensures
availability for released orders.
Requires coordination. Good for
scheduled operations. Reduces
interruption during pick.

**Dynamic:** System-calculated
replenishment based on demand,
lead time, and targets. More
sophisticated. Requires good data.
Review and tune parameters.
"""

version = "0.0.1"
