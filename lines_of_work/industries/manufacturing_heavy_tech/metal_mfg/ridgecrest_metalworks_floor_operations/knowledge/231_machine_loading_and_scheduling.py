title = "Machine Loading and Job Sequencing"

content = """
Machine loading is the process of assigning specific work orders to specific machines within a work center, and job sequencing is the process of determining the order in which those jobs will be run. Together these decisions have a direct impact on setup time, throughput, on-time delivery, and operator utilization.

**Loading principles.** Each machine is loaded up to its available capacity calculated for the period. The cell supervisor uses the SAP production order list, sorted by work center and due date, as the primary scheduling input. Supervisors have authority to resequence jobs within a day without planner involvement, provided no order is moved past its customer due date.

**Sequencing strategies.** Common sequencing rules used at Ridgecrest:

- **Earliest Due Date (EDD):** The job with the nearest due date runs first. Minimizes the number of late jobs. Most common default rule.
- **Critical Ratio (CR):** CR = (days remaining until due date) / (days of work remaining). A CR below 1.0 means the job is already behind schedule. Jobs with the lowest CR run first.
- **Similar setup grouping:** Group jobs with the same material, tooling, or program to reduce setup changeovers. A laser cutting cell running 3 mm carbon steel cuts may sequence all 3 mm jobs consecutively before switching to 6 mm, even if a 6 mm job has a slightly earlier due date—provided the 6 mm due date is not at risk.

**Setup sequence optimization.** For press brake work, sequence bends from tight tolerances to loose tolerances and from complex to simple setups. For CNC machining, sequence material changes from soft to hard alloys where possible to preserve tooling life. For surface treatment lines, sequence light to dark colors to avoid contamination.

**Work-in-process queues.** Each machine has a designated input queue area. Jobs in the queue must be arranged in the planned run sequence, clearly labeled. Never start a job that is not at the front of the queue without supervisor authorization—this commonly causes expedited jobs to bypass sequencing logic and create chaos downstream.

**Replanning triggers.** When a machine goes down, an operator is absent, or a job takes significantly longer than standard time, the supervisor must notify the planner immediately. The planner will reassess load and issue a revised sequence. Operators should not self-assign alternative work without this process.
"""

version = "0.0.1"
