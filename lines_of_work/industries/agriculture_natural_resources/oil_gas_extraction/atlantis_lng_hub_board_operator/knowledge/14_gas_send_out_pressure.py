title = "Pipeline Send-Out Pressure Control"

content = """
Send-out pressure must match the transmission pipeline intake requirements. Pressure control valves at the terminal fence modulate to maintain setpoint. Rapid changes are avoided to prevent pipeline surges.
*   Setpoint: Typically 70 barg unless directed by Transmission Controller.
*   Ramp Rate: Pressure changes limited to 1 barg per minute.
*   Low Trip: Shutdown if pressure drops below 55 barg for 10 seconds.
*   High Trip: Shutdown if pressure exceeds 90 barg.
*   Metering: Ultrasonic flow meters verify volume before handover.
"""  # noqa: E501

version = "0.0.1"
