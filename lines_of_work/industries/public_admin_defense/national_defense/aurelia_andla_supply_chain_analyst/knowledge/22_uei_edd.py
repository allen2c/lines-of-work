title = "UEI, EDD & Routing Identifiers"

content = """
- DoDAAC (Department of Defense Activity Address Code) is the primary routing key. UEI (Unique Entity Identifier) is the federal contractor identification key; the analyst does not maintain UEI data but cross-checks contractor records.
- EDD (Estimated Delivery Date) is the date the storage activity projects the item will be ready to ship; the analyst reconciles EDD vs. RDD (Required Delivery Date) on every priority 04–15 document.
- Where EDD > RDD and the item is priority 06 or higher, the analyst flags the document for a "missed required date" entry but does not cancel the document.
- Routing Identifier Codes (RIC) are verified per transaction; the analyst reports any unverified RIC to the SLOA/SDR cell.
- A matched but inactive RIC returns the document to the requestor with a "RIC status not located" rejection.
"""  # noqa: E501

version = "0.0.1"
