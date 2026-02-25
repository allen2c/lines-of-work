title = "Capacity Planning: Load vs. Available Hours"

content = """
Capacity planning at Ridgecrest Metalworks ensures that the production schedule assigns work to machines and work cells in amounts that can realistically be completed within the planned timeframe. Overloading capacity leads to missed deliveries and overtime; chronic underloading indicates waste and missed revenue. The goal is to match load to available capacity as closely as possible.

**Capacity definition.** Available capacity for a work center is calculated as:
  Available Hours = Shifts per day × Hours per shift × Days in period × Utilization factor × Efficiency factor

- **Utilization** reflects the percentage of shift time the machine is actually available after planned downtime, breaks, and preventive maintenance.
- **Efficiency** reflects the ratio of actual output rates to standard rates, based on historical performance data.

A typical CNC machining center running two 8-hour shifts with 85% utilization and 90% efficiency has about 12.2 available standard hours per day.

**Load calculation.** The load placed on a work center in a given period is the sum of (setup hours + run hours per piece × order quantity) for all work orders scheduled to that center in that period. The load is calculated by SAP's capacity requirements planning (CRP) module.

**Load leveling.** When load exceeds capacity (overload), the planner uses the following levers in priority order:
1. Move orders to an adjacent period where capacity exists (earlier or later, depending on due date constraints).
2. Split the lot and run part of the order at the primary work center and part at an alternate work center with the same capability.
3. Authorize overtime on the overloaded work center.
4. Subcontract the operation to an approved outside processor.

When load is significantly below capacity (underload), the planner may pull future orders forward, schedule preventive maintenance, or authorize cross-training activities.

**Bottleneck identification.** The constraint work center—the one that limits total system throughput—receives special attention. Adding capacity to non-bottleneck work centers does not increase overall output. The scheduling team maintains a daily bottleneck utilization report and ensures the bottleneck is never starved for work.

Capacity planning data is reviewed in the weekly S&OP and in the daily production meeting when any work center is forecast to exceed 100% load within the next 5 days.
"""

version = "0.0.1"
