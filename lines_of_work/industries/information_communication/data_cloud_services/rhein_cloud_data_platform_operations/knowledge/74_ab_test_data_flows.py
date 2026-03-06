title = "A/B Test Data Flows"

content = """
A/B test data requires careful handling to avoid contamination between
variants. Assignment events and outcome events must be joined correctly.
Operations ensure experiment data pipelines run on schedule and maintain
privacy. Statistical significance calculations happen downstream. Failed
pipelines can invalidate experiment results; prioritize these jobs.
"""

version = "0.0.1"
