title = "Putaway Rules Engine"

content = """
Putaway rules automate location assignment when goods are received at Khlong
Siam Merchants. Rules encode business logic for efficient storage.

**Rule types:** Fixed location (item always goes to same place). Random
location (any available slot in zone). Velocity-based (fast movers to
forward areas). Compatibility (hazmat separate, refrigerated in cold zone).
Size-based (bulky items in floor or wide aisles).

**System implementation:** WMS applies rules during putaway. Override when
needed for exceptions. Log decisions for audit. Tune rules based on
performance data.
"""

version = "0.0.1"
