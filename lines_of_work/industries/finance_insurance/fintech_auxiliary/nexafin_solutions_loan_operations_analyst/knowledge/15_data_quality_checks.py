title = "Data Quality Checks"

content = """
- At the start of each shift, run the Data Quality Dashboard in LoanOS. Check for missing fields, inconsistent data (e.g., birth date after application date), and duplicate records.
- For applications with missing SSN or invalid ZIP code, place a hold and request correction from the applicant or partner.
- Reconcile the loan portfolio balance with the general ledger daily. Any difference > 0.5% must be investigated and resolved before end of day.
- Maintain a data quality scorecard: target 99.5% accuracy. Report any recurring issues to the operations manager.
- Use automated validation rules (e.g., SSN format, date ranges) but manually review flagged items.
"""

version = "0.0.1"
