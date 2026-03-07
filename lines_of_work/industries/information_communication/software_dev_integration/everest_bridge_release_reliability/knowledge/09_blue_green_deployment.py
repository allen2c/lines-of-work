"""Blue-green deployment knowledge item."""

title = "Blue-Green Deployment"

content = """
Blue-green deployment maintains two identical production environments. One (e.g. blue)
serves traffic; the other (green) receives the new release. After validation, traffic
switches to green, enabling fast rollback by switching back.

**Environment Setup:** Both environments must be provisioned and ready. Deployment to
the inactive environment does not affect live traffic. Database and shared state require
careful handling: migrations must be backward compatible, or coordinated with the switch.

**Switchover:** The traffic switch can be instant (load balancer config change) or
gradual (canary on top of blue-green). Validate the new environment before switching.
Keep the previous environment available for quick rollback.

**Resource Cost:** Running two full production environments doubles infrastructure cost.
Some organizations use this only for critical services or during release windows.
"""

version = "0.0.1"
