title = "Data Collection and Cleaning"

content = """
- Sources: ERP (sales orders, inventory transactions), WMS (warehouse movements), TMS (freight bills), CRM (customer data). Extract at least 24 months of data.
- Cleaning steps: remove duplicates, handle missing values (interpolate or drop if <5% missing), detect outliers using 3-sigma rule (remove points beyond 3 standard deviations from mean) or IQR method (below Q1-1.5*IQR or above Q3+1.5*IQR).
- Example: sales data for product Y: mean=500, std=100. Any daily sales > 500+3*100=800 or < 500-3*100=200 is flagged as outlier. Investigate: if due to promotion, keep; if data error, correct or remove.
- Document all transformations and assumptions in a data dictionary.
"""  # noqa: E501

version = "0.0.1"
