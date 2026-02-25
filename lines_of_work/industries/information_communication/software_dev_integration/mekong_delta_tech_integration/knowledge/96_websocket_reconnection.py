title = "WebSocket Reconnection"

content = """
WebSocket connection có thể drop. Client cần reconnect logic. Integration
design cho resilience. Mekong Delta Tech document reconnection cho client.

**Detection:** Connection close. Ping/pong fail. Timeout. Network error.
Detect promptly. Don't assume connected. Heartbeat. Monitor.

**Reconnect:** Exponential backoff. Max delay. Jitter. Reconnect attempt.
Reset on success. Persist state (subscription) để resubscribe. Idempotent
subscribe. Don't duplicate.

**State Sync:** After reconnect, sync state. Missed message? Server support
resend? Last event ID? Cursor? Design for gap. Client handle out-of-order.
Idempotent process. Document.

**Testing:** Simulate disconnect. Verify reconnect. State consistency. Load
test. Chaos. Document behavior. Client implement. Support.
"""  # noqa: E501

version = "0.0.1"
