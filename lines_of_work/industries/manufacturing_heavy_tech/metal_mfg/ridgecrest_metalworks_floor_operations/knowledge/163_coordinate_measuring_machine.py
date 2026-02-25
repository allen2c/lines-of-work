title = "Coordinate Measuring Machine (CMM) Operations"

content = """
A Coordinate Measuring Machine (CMM) is a precision measurement instrument that determines the geometry of a part by probing discrete points in three-dimensional space. At Ridgecrest Metalworks, the CMM is used for first article inspection, complex geometric verification, and resolving measurement disputes that hand tools cannot address with sufficient accuracy.

The CMM consists of a precision granite or ceramic table, three perpendicular linear axes driven by servo motors, and a probing system. The touch-trigger probe (ruby ball tip) records the exact coordinates of each point when the probe tip contacts the part surface. A computer runs CMM measurement software (such as PC-DMIS, Calypso, or Renishaw MODUS) that processes the point data to calculate dimensions, form errors, and geometric tolerances.

Setup procedure:
1. The part is cleaned and allowed to thermally stabilize in the CMM room (temperature-controlled to 20 ± 1 °C or better).
2. The part is fixtured on the table using appropriate clamping that replicates the drawing datum scheme without distorting the part.
3. The measurement program is selected or written; the program defines the measurement sequence, probe approach vectors, and measured features.
4. The part coordinate system (part datum reference frame) is established by probing datum features defined on the drawing.
5. The program runs, probing all specified features automatically (for CNC CMMs) or guided by the operator (for manual CMMs).
6. The CMM software generates a dimensional report showing measured values, nominal values, tolerances, and pass/fail status for each feature.

CMM measurement capabilities include:
- Diameter and position of holes and bores
- True position of hole patterns relative to datums (GD&T)
- Flatness, straightness, circularity, and cylindricity
- Perpendicularity, parallelism, and angularity
- Profile of a surface and profile of a line
- Runout (circular and total)

Probe qualification (calibration of the probe ball) is done before each measurement session using a reference sphere. Probe qualification corrects for probe ball radius and establishes the precise position of the probe tip in the machine coordinate system. Any probe change or crash requires immediate re-qualification. The CMM itself undergoes volumetric accuracy verification using a laser interferometer and ball-bar test at defined intervals per ISO 10360.
"""

version = "0.0.1"
