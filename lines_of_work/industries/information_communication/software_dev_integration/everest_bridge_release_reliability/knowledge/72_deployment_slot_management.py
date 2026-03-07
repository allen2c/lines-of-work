"""Deployment slot management for zero-downtime deployments."""

title = "Deployment Slot Management"

content = """
Deployment slots (e.g. blue-green, staging slots) enable swapping traffic between versions
without downtime. Proper slot management ensures clean swaps and avoids resource contention.

**Slot Lifecycle:** Allocate slots for active and standby versions. Deploy to standby first,
run health checks, then swap traffic. After swap, keep the previous slot warm briefly for
quick rollback before deallocating.

**Resource Planning:** Ensure sufficient capacity for both slots during swap. Account for
memory, CPU, and connection limits. Avoid over-provisioning by using autoscaling where
appropriate.

**Validation:** Run smoke tests and synthetic checks against the standby slot before swap.
Verify configuration, secrets, and feature flags. Document swap procedure in runbook.
"""

version = "0.0.1"
