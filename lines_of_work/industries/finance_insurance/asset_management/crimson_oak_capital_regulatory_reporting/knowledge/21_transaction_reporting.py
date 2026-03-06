title = "Transaction Reporting"

content = """
Transaction reporting captures individual trades and positions for regulatory oversight.
Regulators use this data to monitor market abuse, systemic risk, and conduct.

**Reporting Obligations:** MiFID II, EMIR, and SFTR require reporting of derivatives and
securities transactions. Each regime has distinct fields, deadlines, and submission channels.
Asset managers must identify which transactions fall under which regime.

**Data Elements:** Common fields include instrument identifier, counterparty, price, quantity,
execution venue, and timestamp. LEI and ISIN are standard identifiers. Missing or incorrect
identifiers cause rejections and require resubmission.

**Submission Channels:** Trade repositories and approved reporting mechanisms receive
submissions. Firms may delegate to third parties but remain responsible for accuracy.
"""  # noqa: E501

version = "0.0.1"
