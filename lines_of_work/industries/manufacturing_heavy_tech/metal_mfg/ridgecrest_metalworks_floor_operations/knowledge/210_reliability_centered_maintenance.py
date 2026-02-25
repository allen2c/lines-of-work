title = "Reliability-Centered Maintenance (RCM) Principles"

content = """
Reliability-Centered Maintenance (RCM) is an engineering methodology for
developing maintenance strategies based on equipment functions, failure modes,
and the consequences of those failures. Rather than applying a generic
time-based PM schedule to all equipment, RCM asks: "What maintenance tasks are
truly necessary to preserve the function each asset must fulfill?" At Ridgecrest
Metalworks, RCM principles guide how maintenance resources are allocated across
critical and non-critical assets.

**Core RCM Questions (from SAE JA1011):**
1. What are the functions of this asset in its current operating context?
2. In what ways can it fail to fulfill those functions?
3. What causes each functional failure?
4. What happens when each failure occurs?
5. Does each failure matter (safety, environment, production, cost)?
6. What can be done to predict or prevent each failure?
7. What should be done if no suitable proactive task can be found?

**Failure Consequence Categories:**

- **Safety/Environmental:** Failures that could injure personnel or violate
  environmental permits. These receive the highest maintenance priority.

- **Operational:** Failures that stop or significantly degrade production output.
  Preventive and predictive tasks are justified if their cost is less than the
  production loss.

- **Non-Operational:** Failures with no direct safety or production impact.
  Only if the cost of the PM task is less than the cost of the corrective repair
  is proactive maintenance justified.

**Maintenance Task Selection:**
RCM selects the most effective task type for each failure mode:
- **Condition-Based (On-Condition):** Monitor a parameter (vibration, temperature,
  oil analysis) that degrades before the failure point. Act only when the threshold
  is crossed.
- **Time-Based Restoration:** Disassemble and restore to an as-new condition at a
  fixed interval, applied when there is a clear age-related deterioration pattern.
- **Time-Based Discard:** Replace a component at a fixed interval regardless of
  condition, used for items where failure is catastrophic (e.g., safety-critical
  seals, high-wear sacrificial components).
- **Run-to-Failure:** Accept failure and repair reactively when consequences are
  non-safety-related, non-operational, and repair cost is low.

**Floor Application:**
Operators support RCM outcomes by:
- Performing operator rounds that collect condition-based monitoring data (unusual
  sounds, temperature via IR thermometer, oil level and color).
- Reporting early signs of degradation through the CMMS notification system.
- Respecting PM intervals — skipping a PM undermines the RCM logic that justified it.

At Ridgecrest, RCM analysis is reviewed annually by the Engineering and Maintenance
teams, with input from production operators who know their machines best.
"""

version = "0.0.1"
