title = "Rush Order Handling and Schedule Recovery"

content = """
Rush orders are customer-driven or internally generated demands that require accelerated production outside the normal planning cycle. While they are sometimes unavoidable, every unplanned rush has a cost: it disrupts existing schedules, increases setup frequency, drives overtime, and elevates quality risk due to compressed review time. The goal is to manage rush orders systematically rather than chaotically.

**Rush order initiation.** A rush order is formally declared by the production manager or sales manager. Verbal requests from customers or salespeople to individual supervisors do not constitute a rush order authorization. All rush orders must be entered into SAP with a priority flag and a confirmed required date before any schedule disruption is made.

**Impact assessment.** Before committing to a rush, the planner assesses:
- What currently scheduled work will be displaced or delayed?
- Are the required materials in stock or available for emergency purchase?
- Does the required timeline fit within machine and labor capacity, even with overtime?
- Does the rush date conflict with other customer commitments already in place?

The planner provides this assessment in writing to the production manager within 2 hours of a rush request. The production manager decides whether to accept the rush and which existing orders to defer.

**Communication.** When a rush is accepted:
- The planner issues a revised schedule with the rush order clearly marked at priority 1.
- Affected cell supervisors are notified in person, not by email alone.
- Displaced orders' customers are notified by the sales team with revised delivery dates.

**Floor execution.** Rush parts travel with red priority travelers. They jump the input queue and are set up next at the designated machine. Operators must confirm the rush priority with their supervisor before interrupting a current run—mid-process interruptions can cause scrap or quality issues on the job being displaced. When possible, complete the current part or complete a logical stop point before switching.

**Schedule recovery.** After a rush is completed, the planner replaces the displaced work back into the schedule. Recovery overtime is planned for the same week where possible. If multiple orders are displaced and cannot be recovered within the week, customers are contacted proactively before the due dates are missed—not after.

Rush order frequency is tracked monthly. Facilities with high rush frequency are examined for upstream causes: inaccurate forecasting, poor customer communication, or reactive planning processes.
"""

version = "0.0.1"
