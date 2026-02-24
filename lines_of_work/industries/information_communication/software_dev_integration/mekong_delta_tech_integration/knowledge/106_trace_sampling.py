title = "Trace Sampling"

content = """
Full trace mọi request = expensive. Sampling balance cost và visibility.
Mekong Delta Tech configure trace sampling cho integration.

**Strategies:** Fixed rate (1%). Rate limit (N per second). Adaptive (low traffic
100%, high traffic sample). Tail (sample slow, error). Choose per service.
Cost vs insight.

**Head-based vs Tail-based:** Head: decide at start. Consistent trace. Tail:
decide at end. Sample interesting (slow, error). More relevant. Complex.
Both have use.

**Integration:** High volume API. Sample low. Critical path sample higher.
Debug trace on demand (trace ID, force sample). Balance. Tune. Monitor.
Cost. Adjust.

**Correlation:** Sampled trace vẫn có correlation ID. Log link. Can turn on
full trace for debug. Document. Support. Sampling config. Environment.
"""  # noqa: E501

version = "0.0.1"
