title = "EMR and Scheduling System Integration"

content = """
The scheduling system should integrate with the EMR to ensure data consistency
and workflow efficiency. Understand how the systems interact.

**Single Source of Truth:** Schedule in the system that feeds the EMR, or ensure
real-time sync. Duplicate or manual entry leads to errors and double-booking.

**Patient Demographics:** Patient data (name, DOB, insurance) should flow from
registration to scheduling to clinical documentation. Updates in one system
should reflect in the other. Verify sync periodically.

**Appointment Types:** Map scheduling slot types to EMR appointment types and
visit codes. Incorrect mapping causes billing and documentation mismatches.

**Reporting:** Use integrated reporting for utilization, no-show rates, and
therapist productivity. Data from scheduling informs capacity planning and
process improvement.
"""  # noqa: E501

version = "0.0.1"
