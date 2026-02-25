title = "Ticketing System and Workflow Conventions"

content = """
Ganges Valley Tech uses a centralized ticketing system (e.g., Zendesk, Freshdesk, or
Jira Service Management). Consistent usage ensures accountability and accurate metrics.

**Ticket Creation:** Capture full context: customer ID, product, environment, and
initial description. Link to related tickets or incidents when applicable.

**Status Transitions:** Use statuses correctly: New, Open, Pending Customer, Pending
Vendor, Resolved, Closed. Pending states pause SLA when awaiting external response.

**Internal Notes:** Use private notes for internal communication. Customer-visible
replies go in the public thread. Never expose internal discussions or escalation
details to customers.
"""  # noqa: E501

version = "0.0.1"
