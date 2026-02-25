title = "Root Cause Analysis (RCA) for Equipment Failures and Quality Defects"

content = """
Root Cause Analysis (RCA) is a structured problem-solving methodology used at
Ridgecrest Metalworks to identify the fundamental cause of equipment failures or
quality defects — not merely the symptoms — so that the same problem cannot
recur. RCA is triggered for any significant event: major equipment breakdowns,
recurring defects, serious near-misses, or customer complaints requiring 8D
response.

**Common RCA Methods Used on the Floor:**

**1. 5-Why Analysis:**
The simplest and most widely used tool. Ask "Why?" repeatedly until the root
cause is reached, typically within 3–6 levels. Example:
- Why did the bearing fail? — Insufficient lubrication.
- Why was lubrication insufficient? — Auto-lubricator blocked.
- Why was the lubricator blocked? — Metal swarf entered the grease line.
- Why did swarf enter? — Grease fitting cover was missing after last maintenance.
- Root cause: Maintenance task checklist did not include "replace grease fitting
  cover."

**2. Fishbone (Ishikawa) Diagram:**
A visual tool that organizes potential causes into six categories: Machine, Method,
Material, Man, Measurement, and Environment (the 6Ms). Used for more complex
failures where multiple contributory causes are suspected. The team brainstorms
causes in each category before drilling into the most likely root causes.

**3. Fault Tree Analysis (FTA):**
A top-down, deductive method using logic gates (AND/OR) to map all combinations
of events that could lead to an undesired outcome. Used for safety-critical
equipment failures or complex multi-cause scenarios.

**4. Is/Is-Not Analysis:**
Defines the problem by contrasting what it IS with what it IS NOT, narrowing
the investigation scope. Useful when the failure occurs on some machines but
not others, in some shifts but not others.

**RCA Process Steps:**
1. Define the problem clearly with data: what happened, when, how often, impact.
2. Collect physical evidence, maintenance records, and operator statements while
   the evidence is fresh.
3. Assemble a cross-functional team (operator, maintenance tech, quality engineer).
4. Apply the selected RCA tool.
5. Validate the root cause: if the root cause is corrected, does the problem stop?
6. Develop a corrective action plan with owner, action, and due date.
7. Verify effectiveness after implementation; close the CAPA record.

**Documentation:**
All RCA findings are documented in the CAPA system with a reference to the
originating work order or NCR. Records are retained for a minimum of five years.
"""

version = "0.0.1"
