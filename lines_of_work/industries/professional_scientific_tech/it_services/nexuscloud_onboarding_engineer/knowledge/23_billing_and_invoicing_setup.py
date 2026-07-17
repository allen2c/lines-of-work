title = "Billing and Invoicing Setup"

content = """
- Customer must set up billing profile in cloud provider: payment method, tax ID, and budget limit. Engineer verifies during prerequisites.
- NexusCloud charges are separate: monthly fee based on tier plus resource consumption. Invoiced via NexusCloud Billing Portal.
- Engineer must enable cost allocation tags (see knowledge item 07) to ensure accurate billing.
- For Enterprise, set up consolidated billing across multiple accounts. Use AWS Organizations or Azure Management Groups.
- If customer fails to set up billing, onboarding cannot proceed. Escalate to finance team after 5 business days.
"""

version = "0.0.1"
