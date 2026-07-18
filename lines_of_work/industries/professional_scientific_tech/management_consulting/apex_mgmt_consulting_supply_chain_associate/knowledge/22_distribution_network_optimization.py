title = "Distribution Network Optimization"

content = """
- Use optimization models: linear programming (LP) for flow allocation, mixed-integer programming (MIP) for facility location decisions. Objective: minimize total cost (transportation + inventory + facility fixed costs) subject to service level constraints (e.g., 95% of demand within 2 days).
- Example: 3 potential DC locations, 50 customer zones. Solve MIP to select 2 DCs that minimize cost. Use software (Llamasoft, AIMMS, or Python with PuLP).
- Sensitivity analysis: test scenarios (e.g., fuel cost +20%, demand growth 10%). Identify robust network configuration.
- Key outputs: number and location of DCs, assignment of customers to DCs, transportation mode mix, inventory levels per DC.
"""  # noqa: E501

version = "0.0.1"
