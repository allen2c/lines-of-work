title = "Authorization Tracking and Renewal"

content = """
Tracking authorizations prevents scheduling visits that will not be covered.
Proactive renewal avoids gaps in care and patient disappointment.

**Tracking Fields:** For each authorization, record the authorization number,
effective dates, visit limit, procedure codes (if applicable), and payer
contact. Store in the EMR or a dedicated tracking tool linked to the patient.

**Visit Counting:** Count visits used against the authorization limit. Update
after each billed visit. When within 1–2 visits of the limit, trigger the
renewal process. Do not schedule beyond the limit without a new authorization.

**Renewal Process:** Request renewal with updated clinical justification
(e.g., progress note, reassessment). Submit per payer requirements and
timing (some payers require submission before the last authorized visit).
Follow up until approval is received.

**Expiration Alerts:** Set reminders for authorization expiration dates.
Contact the therapist and patient when an authorization is about to expire
and renewal has not been approved.
"""  # noqa: E501

version = "0.0.1"
