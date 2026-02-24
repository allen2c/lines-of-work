title = "Options Strategies"

content = """
Options strategies employ call and put options in various combinations to achieve specific risk-return profiles, enabling sophisticated market positioning for directional views, volatility plays, and risk management objectives.

**Basic Strategies:**
- **Long Call**: Profits from underlying price increases, limited risk equals premium paid
- **Long Put**: Profits from underlying price decreases, limited risk equals premium paid  
- **Covered Call**: Generates income by selling calls against owned stock, caps upside potential
- **Protective Put**: Insures stock holdings against downside risk, costs equal to put premium

**Spread Strategies:**
- **Bull Call Spread**: Combines long call and short higher-strike call, limited profit and loss
- **Bear Put Spread**: Combines long put and short lower-strike put, limited risk-reward profile
- **Calendar Spread**: Sells near-term options, buys longer-term options, profits from time decay
- **Diagonal Spread**: Combines different strikes and expirations for directional bias with time decay

**Combination Strategies:**
- **Straddle**: Long call and put at same strike, profits from large price moves in either direction
- **Strangle**: Long call and put at different strikes, profits from large price moves beyond breakeven points
- **Butterfly Spread**: Combines bull and bear spreads, profits from price stability near middle strike
- **Condor Spread**: Wider butterfly with four strike prices, profits from price stability within range

**Volatility Strategies:**
- **Long Straddle/Strangle**: Profits from increased volatility, losses from stability
- **Short Straddle/Strangle**: Profits from decreased volatility, unlimited risk from large moves
- **Iron Condor**: Sells out-of-money calls and puts, profits from stability within defined range

**Advanced Strategies:**
- **Collar**: Combines covered call with protective put, limits both upside and downside
- **Ratio Spreads**: Unequal position sizes create directional bias with defined risk-reward
- **Synthetic Positions**: Replicate stock positions using options (synthetic long stock = long call + short put)

**Greeks Analysis:**
- **Delta**: Measures directional sensitivity and position hedge ratios
- **Gamma**: Measures delta change rate, important for dynamic hedging
- **Theta**: Measures time decay impact on position value
- **Vega**: Measures sensitivity to volatility changes
- **Rho**: Measures sensitivity to interest rate changes

**Risk Management:** Requires monitoring position greeks, adjusting hedges, and implementing stop-loss mechanisms to control losses during adverse market movements.

Options strategies enable precise risk management and market positioning when properly implemented with comprehensive risk controls.
"""

version = "0.0.1"
