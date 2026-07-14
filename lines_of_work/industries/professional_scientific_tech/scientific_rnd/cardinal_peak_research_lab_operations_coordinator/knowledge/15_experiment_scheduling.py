title = "Study and Experiment Scheduling"

content = """
- Translate approved study protocols into an executable schedule: which analyses run
  when, on which instrument, with which analyst, against which sample-stability and
  sponsor-deadline windows.
- Sequence work around constraints: sample hold times, reagent and standard availability,
  instrument calibration status, analyst qualification, and required QC runs. A run
  should not be scheduled if any prerequisite is missing.
- Coordinate multi-step studies so that outputs of one step feed the next without samples
  aging out or bottlenecks forming at a single shared instrument.
- Build in QC and system-suitability runs, blanks, and controls as part of the schedule,
  not as afterthoughts, since they gate whether the analytical run is valid.
- Keep a realistic buffer for reruns, maintenance, and the unexpected. Over-packed
  schedules cause corner-cutting, which is where data-integrity and safety problems
  start.
- Publish the schedule where the team can see it, update it as reality changes, and flag
  slippage early to Study Directors so sponsors get honest timelines.
"""

version = "0.0.1"
