title = "Fraud Prevention: Positive Pay and ACH Blocks"

content = """
In an era of increasing sophisticated financial crime, Silver Oak Bank provides
robust fraud prevention tools to protect corporate deposits. Positive Pay and
ACH Blocks/Filters are the industry standards for securing business accounts.

**Positive Pay (Check Fraud Prevention):**
The client provides the bank with a 'check issue file' containing the check
number, date, and amount of all checks issued. When a check is presented for
payment, the bank compares it against the file. If any detail doesn't match, the
check is flagged as an exception, and the client must decide whether to 'pay' or
'return' the item via the online banking portal.

**ACH Blocks and Filters:**
- **ACH Block:** Prevents all ACH debits from posting to an account. This is
  ideal for accounts used exclusively for deposits or internal transfers.
- **ACH Filter:** Allows only authorized vendors (identified by their Company ID)
  to debit the account, up to a specified dollar limit.

**Best Practices:**
Clients should reconcile their accounts daily and use dedicated computers for
online banking to mitigate the risk of malware-based account takeover.
"""

version = "0.0.1"
