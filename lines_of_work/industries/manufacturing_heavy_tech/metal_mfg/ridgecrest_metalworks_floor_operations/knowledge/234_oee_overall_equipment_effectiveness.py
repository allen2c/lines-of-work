title = "OEE: Availability, Performance, and Quality"

content = """
Overall Equipment Effectiveness (OEE) is the primary metric for measuring how productively a machine or production line is being used relative to its full potential. At Ridgecrest Metalworks, OEE is calculated for every key work center and displayed on cell performance boards, updated daily.

**OEE formula.** OEE = Availability × Performance × Quality

**Availability** measures the proportion of planned production time that the machine was actually running:
  Availability = (Planned Production Time – Unplanned Downtime) / Planned Production Time
  Example: If planned time is 480 min and unplanned downtime is 60 min, Availability = 420/480 = 87.5%

**Performance** measures how fast the machine ran compared to its theoretical maximum (ideal cycle time):
  Performance = (Ideal Cycle Time × Total Pieces Produced) / Operating Time
  A machine running at 80 part/hr against a standard of 100 part/hr has Performance = 80%
  Performance losses include slow running (speed losses) and minor stoppages (less than 10 minutes).

**Quality** measures the proportion of parts produced that are first-pass conforming (no rework or scrap):
  Quality = Good Parts / Total Parts Produced
  A machine producing 1,000 parts with 50 scrap and 20 rework has Quality = 930/1,000 = 93%

**OEE calculation example:**
  Availability 87.5% × Performance 80% × Quality 93% = OEE 65%

**World-class benchmarks.** A world-class OEE for a discrete metal manufacturing operation is considered 85% or above. Ridgecrest's current facility target is 75% for existing equipment, with a long-term goal of 80%. Cells below 65% are on formal improvement plans.

**Six Big Losses framework.** OEE losses are categorized into six types:
1. Equipment failures (Availability)
2. Setups and adjustments (Availability)
3. Idling and minor stoppages (Performance)
4. Reduced speed (Performance)
5. Process defects (Quality)
6. Startup and yield losses (Quality)

Each loss category has specific countermeasures. The cell team identifies which of the six losses is largest using the weekly OEE data and focuses improvement energy there.

OEE data integrity depends entirely on accurate downtime, production count, and scrap recording by operators.
"""

version = "0.0.1"
