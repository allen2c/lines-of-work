title = "System Integration"

content = """
- NexaFin's platform integrates with credit bureaus (Experian, Equifax, TransUnion), KYC providers (Jumio, Onfido), AML screening (LexisNexis), and payment gateways (Stripe, Plaid).
- If an integration fails (e.g., credit report not returned), check the API status dashboard. If the issue persists > 15 minutes, escalate to IT.
- For batch processing (e.g., daily ACH file), verify that the file was generated and transmitted successfully. Confirm receipt with the bank.
- When a new partner bank is onboarded, test the integration with a dummy loan before going live.
- Document any integration errors and resolutions in the shared knowledge base.
"""

version = "0.0.1"
