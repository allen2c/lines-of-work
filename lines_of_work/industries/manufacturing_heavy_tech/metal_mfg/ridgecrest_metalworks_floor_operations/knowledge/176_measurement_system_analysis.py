title = "Measurement System Analysis (MSA) and Gauge R&R"

content = """
Measurement System Analysis (MSA) is a statistical method for evaluating the performance of a measurement system. Before trusting measurement data for process control or product acceptance decisions, it is necessary to verify that the measurement system itself is capable — that is, it introduces acceptable variation relative to the tolerance being measured. At Ridgecrest Metalworks, MSA is required for all measurement systems used in SPC and for critical characteristics on new part launches.

The key concept of MSA is that measured values contain both actual part variation and measurement error. Measurement error has two components:
- Repeatability (equipment variation, EV): Variation in readings obtained by the same operator measuring the same part multiple times with the same instrument. This reflects the instrument's inherent variation.
- Reproducibility (appraiser variation, AV): Variation in readings obtained by different operators measuring the same parts with the same instrument. This reflects operator-to-operator technique differences.

Gauge Repeatability and Reproducibility (Gauge R&R) study: The standard method involves multiple appraisers (typically 2–3), each measuring a sample of parts (typically 10) multiple times (typically 2–3 replicates), in a randomized order. The data is analyzed using ANOVA or the range method (per AIAG MSA manual). The results express measurement variation as a percentage of:
- Study variation (% R&R): Measurement variation as a percentage of total observed variation (part variation + measurement variation). This assesses fitness for process control.
- Tolerance (% P/T): Measurement variation as a percentage of the drawing tolerance. This assesses fitness for product acceptance.

Acceptance criteria at Ridgecrest (per AIAG guidelines):
- %R&R < 10 %: Measurement system is acceptable
- %R&R 10–30 %: Conditionally acceptable; decision depends on application criticality
- %R&R > 30 %: Measurement system is not acceptable; must be improved before use for SPC or acceptance decisions

Measurement bias, linearity, and stability are also assessed in full MSA studies. Bias compares average readings against a reference value; linearity checks if bias is consistent across the measurement range; stability monitors gauge performance over time.

MSA records are maintained in the quality system and reviewed when gauges are repaired, replaced, or when operator personnel changes significantly affect the measurement system.
"""

version = "0.0.1"
