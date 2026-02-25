title = "Basic Job Costing and Floor Input for Quoting"

content = """
Job costing at Ridgecrest Metalworks is the process of accumulating all costs incurred to manufacture a specific work order and comparing those actual costs against the estimated (standard) cost that was used to price the job. Floor personnel are not responsible for final quoting, but their accurate time and material reporting is the input that makes job costing meaningful.

**Cost components of a production order.**

1. **Material cost.** The cost of raw material consumed, based on the quantity issued (goods issue transaction) multiplied by the standard material price. Material yield is important—excessive scrap drives actual material cost above standard.

2. **Direct labor cost.** The time each operator spends at each routing operation, multiplied by that work center's labor rate. This time is recorded through production confirmations (scanning in and out at operations). Inaccurate time reporting creates phantom variances that make it impossible to identify genuine efficiency problems.

3. **Machine overhead.** Applied overhead rate (dollars per machine-hour or per direct labor hour) covering machine depreciation, energy, tooling amortization, and facility costs. Applied automatically in SAP based on actual hours confirmed.

4. **Setup cost.** Recorded separately in many cases, particularly for high-setup operations like press brake or CNC machining. Setup time is entered by the operator at the start of each production order setup.

**Floor contribution to accurate costing.** Operators contribute to cost accuracy by:
- Confirming production quantities accurately (no rounding to "full pallets").
- Recording scrap with correct scrap codes at the time of occurrence.
- Starting and stopping operation confirmations at the correct times.
- Not reporting production on the wrong work order number.

**How quoting uses floor data.** When estimating a new job, the estimating team pulls historical actual cost data from similar completed work orders. If actual costs are consistently above standard due to unreported scrap or inaccurate time entries, the estimating database is corrupted and new quotes will be underpriced, resulting in losses.

**Variance reporting.** After a work order closes, the finance team reviews production variances: labor efficiency variance (actual hours vs. standard hours), material usage variance (actual material consumed vs. standard), and scrap variance. Variances above ±10% of standard cost require a floor-level explanation from the supervisor.
"""

version = "0.0.1"
