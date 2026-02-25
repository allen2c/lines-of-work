title = "Tick Size Rules"

content = """
Tick size rules define minimum price increments for order placement.
HKEX and other exchanges specify tick sizes by price band.

**Price Bands** group securities by price level. Lower-priced
securities typically have smaller absolute tick sizes but may
have larger percentage increments.

**Order Placement** must respect tick size. Orders at invalid
prices may be rejected or rounded.

**Strategy** implications: Tick size affects market making
spreads and algorithmic execution. Very large tick sizes can
reduce liquidity.

**Changes** to tick size rules occur periodically. Monitoring
exchange announcements maintains compliance.
"""

version = "0.0.1"
