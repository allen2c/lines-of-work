title = "Order Types and Execution Methods"

content = """
Order types and execution methods form the foundation of securities trading. Understanding
these mechanisms is essential for optimizing execution quality and managing trading costs
on HKEX and other venues.

**Market Orders** direct brokers to buy or sell immediately at the best available price.
They prioritize speed over price certainty. In fast-moving markets, market orders can
result in slippage.

**Limit Orders** specify a maximum purchase price or minimum sale price, providing price
protection but no execution guarantee. Time-in-force options include day, GTC, and IOC.

**Stop Orders** trigger market orders when a specified price level is reached, used for
loss mitigation or momentum strategies. Stop-loss and stop-limit orders provide different
execution controls.

**Execution Algorithms** break large orders into smaller components. VWAP targets average
price weighted by volume. TWAP distributes execution evenly. Implementation shortfall
algorithms minimize market impact dynamically.

**Smart Order Routing** directs orders to optimal venues based on liquidity, costs, speed,
and price improvement. Systems monitor HKEX, dark pools, and crossing networks.
"""

version = "0.0.1"
