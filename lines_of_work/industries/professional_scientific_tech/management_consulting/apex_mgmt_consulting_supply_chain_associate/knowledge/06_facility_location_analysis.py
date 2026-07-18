title = "Facility Location Analysis"

content = """
- Factors: customer demand density, supplier proximity, labor availability and cost, taxes, real estate costs, infrastructure (ports, highways), regulatory environment.
- Method: weighted scoring model. Assign weights (0-1) to criteria, score each candidate location (1-10), compute weighted sum. Example: weight for demand proximity=0.4, labor cost=0.3, infrastructure=0.2, taxes=0.1. Location A scores 8,6,7,5 → total = 8*0.4+6*0.3+7*0.2+5*0.1 = 3.2+1.8+1.4+0.5=6.9.
- For quantitative analysis, use center-of-gravity method: optimal location coordinates = (Σ wi xi / Σ wi, Σ wi yi / Σ wi) where wi = demand weight, (xi,yi) = customer coordinates.
"""  # noqa: E501

version = "0.0.1"
