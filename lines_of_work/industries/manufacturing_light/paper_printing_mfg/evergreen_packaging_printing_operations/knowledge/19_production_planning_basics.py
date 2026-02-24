"""
Knowledge about production planning fundamentals for packaging operations.
"""

title = "Production Planning Basics"

content = """
Production planning transforms customer orders into efficient production
schedules that meet delivery commitments while maximizing equipment
utilization and minimizing costs.

**Order Aggregation:** Similar jobs group together to reduce changeover.
Jobs sharing substrates, formats, or colors sequence together. Gang runs
combine multiple small orders on shared press sheets. Aggregate planning
balances the efficiency of long runs against inventory carrying costs and
customer flexibility needs.

**Capacity Planning:** Available press hours must match production requirements.
Planning considers: scheduled maintenance windows; estimated makeready and
run speeds; historical spoilage rates; operator availability. Capacity
models predict bottlenecks and guide overtime decisions or outsourcing.
Finite capacity scheduling recognizes that multiple jobs cannot occupy the
same press simultaneously.

**Sequencing Logic:** Job sequence impacts efficiency. Shortest processing
time first reduces work-in-process. Earliest due date prioritization meets
customer commitments. Changeover minimization groups compatible jobs. Critical
ratio (time remaining divided by work remaining) identifies urgent orders.
Advanced systems use optimization algorithms balancing multiple objectives.

**Schedule Communication:** Published schedules communicate commitments to
production teams, customer service, and management. Visual management boards
display current status. Electronic notifications update stakeholders when
conditions change. Clear communication enables proactive response to disruptions.

**Schedule Adherence and Recovery:** Actual production deviates from plans
due to equipment failures, quality issues, or priority changes. Recovery
actions include: reassigning jobs to alternate equipment; splitting jobs
across multiple presses; expediting critical orders; communicating delays
to affected customers. Resilience distinguishes effective planning systems.
"""

version = "0.0.1"
