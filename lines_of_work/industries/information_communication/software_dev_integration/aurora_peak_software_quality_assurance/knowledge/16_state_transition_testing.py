title = "State Transition Testing for Workflows"

content = """
Financial workflows often involve states: order pending, paid, shipped;
loan application, approved, disbursed. State transition testing
validates that the system correctly handles valid and invalid transitions.

**State Diagram:** We model workflows as state diagrams. Each state
has defined entry conditions, exit conditions, and permitted
transitions. Invalid transitions (e.g., paid to pending) must
be rejected.

**Test Design:** We test every valid transition at least once.
We test invalid transitions to ensure they are rejected with
appropriate errors. We test boundary conditions: concurrent
transitions, timeouts, and rollbacks.

**Implementation:** State machines in code should have corresponding
tests. We use table-driven or parameterized tests to cover
transition matrices efficiently.
"""  # noqa: E501

version = "0.0.1"
