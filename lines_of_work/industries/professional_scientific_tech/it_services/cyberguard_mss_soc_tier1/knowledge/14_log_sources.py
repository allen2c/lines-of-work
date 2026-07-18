title = "Common Log Sources & Their Importance"

content = """
- **Firewall logs** (Palo Alto, Fortinet): show allowed/blocked traffic, source/destination IPs, ports.
- **Proxy logs** (Zscaler, Blue Coat): show web requests, categories, and user identity.
- **Active Directory logs**: authentication events (4624 success, 4625 failure), account changes, group membership modifications.
- **DNS logs**: queries to known malicious domains, high volume of NXDOMAIN responses.
- **Cloud logs** (AWS CloudTrail, Azure Audit): API calls, S3 bucket access, IAM changes.
- **Endpoint logs** (CrowdStrike, Windows Event Logs): process creation, file modifications, registry changes.
- When triaging, always correlate across at least two log sources to confirm an event.
"""

version = "0.0.1"
