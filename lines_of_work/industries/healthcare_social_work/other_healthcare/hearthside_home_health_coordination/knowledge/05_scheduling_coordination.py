title = "Caregiver Scheduling and Visit Coordination"

content = """
Scheduling is one of the most operationally demanding aspects of home health coordination. Unlike
facility-based care, home health visits must account for geographic distance, clinician availability,
patient preferences, and insurance-mandated visit frequencies — all while maintaining clinical continuity.

**Scheduling Principles**
- *Continuity of care:* Assign the same clinician to a patient whenever possible. Familiarity improves
  assessment accuracy and patient trust.
- *Frequency compliance:* Match visit frequency exactly to physician orders. Over-visiting without orders
  is a billing risk; under-visiting may compromise clinical outcomes.
- *Geographic efficiency:* Group clinician visits by zone to minimize travel time and prevent burnout.
- *Patient preference:* Accommodate preferred visit times when clinically flexible, but do not let
  preference override clinical necessity.

**Building the Weekly Schedule**
At the start of each week, generate a visit schedule in the scheduling module of the EMR. Confirm
clinician availability, account for holidays and PTO, and flag any patient whose frequency window
closes within the next 48 hours. Share the schedule with clinical staff by end of day Monday for the
upcoming week.

**Managing Cancellations and No-Shows**
When a patient cancels or a clinician calls out, act immediately:
1. Determine whether the missed visit is clinically urgent (wound care, IV therapy, early post-discharge).
2. If urgent, reassign to an on-call clinician the same day.
3. If non-urgent, reschedule within the compliance window for the visit frequency ordered.
4. Document the cancellation reason and rescheduled date in the EMR visit log.

**Same-Day Coverage**
Maintain an on-call roster of staff available for same-day urgent visits. Verify on-call availability
at the start of each week. Ensure on-call clinicians have access to patient records and have reviewed
any active safety alerts before taking an assignment.

**Tracking and Reporting**
Run a missed-visit report weekly. Any patient with two or more consecutive missed visits should be
reviewed by the clinical supervisor and, if clinically warranted, a wellness check or phone call
should be arranged.
"""

version = "0.0.1"
