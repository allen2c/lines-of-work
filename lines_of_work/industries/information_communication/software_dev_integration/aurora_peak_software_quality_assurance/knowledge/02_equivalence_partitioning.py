title = "Equivalence Partitioning and Boundary Analysis"

content = """
Equivalence partitioning divides input data into classes of equivalent behavior.
Tests designed from one value in each partition can efficiently cover the range.
Boundary analysis extends this by focusing on values at partition edges.

**Partition Identification:** Valid and invalid input ranges define partitions.
For example, an amount field might have partitions: negative (invalid), zero
(valid edge), positive (valid), and overflow (invalid). One test per partition
reduces redundancy while maintaining coverage.

**Boundary Values:** Defects often cluster at boundaries. Test both the last
valid value and the first invalid value for each boundary. For a limit of
1000, test 999, 1000, and 1001 explicitly.

**Financial Domain Application:** Transaction amounts, date ranges, account
IDs, and currency codes all have natural partitions. Applying this technique
systematically reduces gaps in financial validation logic.
"""  # noqa: E501

version = "0.0.1"
