title = "Algorithmic Trading Strategies"

content = """
Algorithmic trading strategies automate order execution using predefined rules and
real-time market data. They reduce market impact and improve execution quality for
institutional order flow.

**VWAP** targets execution at the volume-weighted average price. Orders are paced
according to historical volume patterns throughout the session.

**TWAP** distributes execution evenly across time. Suitable when volume patterns are
uncertain or when minimizing timing risk is the priority.

**Implementation Shortfall** minimizes the difference between execution price and
decision price. Algorithms adapt to real-time market conditions and opportunity cost.

**POV (Percentage of Volume)** executes as a fixed percentage of market volume.
Reduces market impact by blending with natural flow.

**Sniper Algorithms** seek immediate execution when liquidity appears. Used for
opportunistic fills when patience is not warranted.
"""

version = "0.0.1"
