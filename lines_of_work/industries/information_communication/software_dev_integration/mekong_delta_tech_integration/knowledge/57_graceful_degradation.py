title = "Graceful Degradation"

content = """
Khi dependency fail, system degrade gracefully thay vì crash. Core function
duy trì. Mekong Delta Tech design integration cho degradation.

**Fallback:** Optional data từ cache khi API down. Default value. Reduced
feature. Queue request cho retry sau. Circuit breaker stop calling failed
service. Return partial response với notice.

**Prioritization:** Critical path vs nice-to-have. Critical: auth, payment.
Degrade non-critical first. Feature flag để disable non-essential. Document
degradation behavior.

**User Experience:** Clear message khi degraded. Không silent failure. Retry
option. Support contact. Status page. Don't show technical error to user.

**Recovery:** Auto-recovery khi dependency heal. Circuit half-open test.
Re-enable feature. Verify. Monitor recovery. Post-incident review degradation
handling.
"""  # noqa: E501

version = "0.0.1"
