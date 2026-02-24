"""Critical path method for development project scheduling."""

title = "Critical Path Method"

content = """
The critical path is the longest sequence of dependent activities from project start to
finish. Activities on the critical path have zero float; any delay directly impacts
the project completion date.

**Identifying Critical Path:** After defining activities and dependencies, perform
forward and backward pass calculations to determine early start, early finish, late
start, and late finish for each activity. Activities with zero total float form the
critical path.

**Float and Slack:** Total float is the amount of time an activity can be delayed
without affecting the project end date. Free float is delay allowed without affecting
succeeding activities. Near-critical paths with low float warrant close monitoring.

**Compression and Recovery:** When delays occur, evaluate crashing (adding resources)
or fast-tracking (overlapping activities) on the critical path. Document trade-offs
between cost, risk, and schedule benefit before implementing recovery measures.

**Communicating Impact:** Clearly report which activities are on the critical path and
how delays propagate. Help stakeholders prioritize attention and resources on
critical-path items.
"""

version = "0.0.1"
