title = "Spot Rate vs Contract Rate Decision Logic"

content = """
- Use contract rate when load matches existing lane, volume ≥ 80 % of forecast, and carrier has capacity commitment.  
- Switch to spot when: lane not in contract portfolio, carrier capacity < 50 % of required equipment, or market spot rate ≤ contract rate – 5 %.  
- Decision engine in TMS runs nightly; outputs “Rate Recommendation” flag (Contract/Spot) with variance percentage.  
- Coordinator validates recommendation; overrides logged with justification (e.g., special equipment, time‑critical).  
- Spot loads tracked separately in KPI “Spot Utilization %” target ≤ 15 % of total loads.
"""  # noqa: E501

version = "0.0.1"
