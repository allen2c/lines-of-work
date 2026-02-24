title = "Feature Flags"

content = """
Feature flag enable/disable feature without deploy. Integration rollout, A/B test,
kill switch. Mekong Delta Tech dùng feature flag cho integration control.

**Use Cases:** Gradual rollout. Canary. Partner-specific enable. Deprecation.
Emergency disable. Experiment. Configuration without code change.

**Implementation:** Flag service (LaunchDarkly, custom). Check at runtime.
Context (user, partner, env). Evaluate. Cache. Low latency. Fallback when
service down. Default safe.

**Integration:** New integration behind flag. Enable for pilot partners.
Monitor. Full rollout. Remove flag when stable. Document flag. Cleanup
old flags. Flag hygiene.

**Best Practice:** Short-lived flag. Document purpose. Owner. Sunset plan.
Don't proliferate. Audit. Test both states. Flag as code.
"""  # noqa: E501

version = "0.0.1"
