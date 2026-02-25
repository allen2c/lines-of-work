title = "Master Production Schedule (MPS) and Capacity"

content = """
The Master Production Schedule (MPS) is the formal statement of what Ridgecrest Metalworks plans to produce, in what quantities, and in what time periods. It is the central commitment that drives all downstream planning—materials procurement, labor allocation, and machine scheduling. An achievable, realistic MPS is one of the most important conditions for stable production operations.

**MPS inputs.** The MPS is built from:
- Customer sales orders (firm demand with due dates)
- Forecast for standard products (statistical or customer-provided)
- Finished goods inventory targets
- Available-to-promise (ATP) commitments made by sales
- Backlog carryover from previous periods

**Time fences.** The MPS is divided into planning horizons protected by time fences:
- Demand time fence (typically 2 weeks): Inside this fence, changes are frozen except for urgent customer or management overrides. Changes inside the demand fence require supervisor and planning manager approval.
- Planning time fence (typically 6–8 weeks): MRP regeneration and routine planner adjustments occur within this horizon. Beyond the planning fence, the plan is tentative and subject to revision.

**Rough-cut capacity planning (RCCP).** Before finalizing the MPS, planners run RCCP to verify that the schedule does not exceed available capacity at critical work centers (the bottleneck machines). RCCP uses a simplified capacity model comparing planned output hours against available hours by period. An overloaded MPS must be adjusted by moving orders, splitting lots, authorizing overtime, or subcontracting before it is released to the shop floor.

**MPS stability.** Frequent changes to the MPS within the demand time fence are called "nervousness" and they destroy production efficiency. Setup changes, material expediting, and overtime costs all increase when the MPS is unstable. The planner's primary obligation is to change the MPS as infrequently as possible and to absorb reasonable demand fluctuation within available buffers before revising.

**Communication of changes.** When an MPS change is unavoidable, the planner communicates the change to the affected cell supervisor with a minimum of 24 hours lead time whenever possible. The supervisor then adjusts the detailed schedule and communicates to operators at the next shift meeting.

MPS adherence (planned vs. actual quantity in the period) is a key KPI reviewed in the weekly operations meeting.
"""

version = "0.0.1"
