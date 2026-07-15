title = "Foot Traffic Sensor System and Data Interpretation"

content = """
- Oakwood Mall uses 40+ infrared people counters at all entrances and major corridors. Data feeds into a dashboard (TrafficAnalytics Pro) updated every 15 minutes.
- Key metrics: Total visits, dwell time (average minutes per visit), conversion rate (estimated from POS data shared by tenants – opt-in only), and traffic by zone (e.g., food court, fashion wing).
- Daily report generated at 9:00 AM for previous day. Weekly report every Monday with comparison to same week last year and forecast for upcoming week.
- Anomaly detection: If any zone shows >30% drop from 7-day rolling average, system sends alert. Investigate within 2 hours – check for construction, event conflicts, or sensor malfunction.
- Data retention: Raw data kept for 2 years; aggregated reports kept for 5 years. Do not share individual tenant sales data – only aggregated traffic.
"""

version = "0.0.1"
