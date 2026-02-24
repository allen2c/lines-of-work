title = "Machine Setup and First Article Inspection"

content = """
Proper machine setup establishes the foundation for accurate, repeatable machining.
Skipping or rushing setup procedures leads to scrap, rework, and safety hazards.

**Pre-Operation Checks:**
Verify machine status (no alarms, maintenance complete). Check coolant level and
concentration. Inspect spindle and tool changer for debris or damage. Confirm
work area cleanliness and chip disposal system function.

**Tool Loading and Verification:**
Load tools into the magazine according to the tool list. Verify tool numbers,
descriptions, and preset lengths. Use a tool presetter or on-machine probing to
measure and record tool length offsets (H offsets) and diameter values (D offsets)
for cutter compensation.

**Work Coordinate System (WCS) Setup:**
Establish the part zero location using an edge finder, touch probe, or manual
indication. Set the WCS offset (G54-G59.3) to match the programmed origin. For
multiple fixtures, set additional WCS offsets for each position. Verify by
running a dry cycle or using probe verification routines.

**Fixture Installation:**
Mount and secure the fixture to the machine table. Verify fixture cleanliness
and condition. Load the workpiece and apply appropriate clamping force. Confirm
the part is fully seated against locators and that clamps do not interfere with
toolpaths.

**First Article Inspection:**
Before production release, machine a single part and verify all critical
dimensions against the drawing. Use calibrated instruments appropriate for the
tolerances. Document measurements on an inspection report. Compare results to
tolerance bands and calculate Cpk if required by the quality plan.

**Test Cuts and Adjustments:**
For critical surfaces, make test cuts on scrap material or excess stock. Adjust
tool offsets based on measured results (wear compensation). Verify surface finish
meets requirements before committing to full depth cuts.

**Program Verification:**
Perform a dry run (no workpiece or spindle off) to verify toolpaths. Use single
block mode and reduced feed override for the first production run. Watch for
unexpected motions, rapid into workpiece, or tool interference with fixtures.

**Production Release:**
Once first article passes inspection and program verification is complete,
authorize production. Set inspection frequency (100%, statistical sampling,
or in-process) based on feature criticality and process capability.
"""

version = "0.0.1"
