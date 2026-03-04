title = "LOD Matrix"

content = """
LOD matrix mendefinisikan Level of Development per element type dan project phase.
Matrix: rows = element (wall, column, duct), columns = phase (DD, CD, IFC, as-built).
Cell = LOD number. Ensures clarity: what detail when. Different systems may have
different LOD at same phase—e.g., structure LOD 300 at CD, MEP LOD 350. Matrix
in BEP. Prevents over-modeling (waste) dan under-modeling (insufficient for coordination).
"""  # noqa: E501

version = "0.0.1"
