title = "LNG Unloading Flow Rate Management"

content = """
Unloading rates are ramped up gradually to prevent thermal shock to the ship's manifold and terminal piping. The Board Operator controls the main isolation valves and flow control valves from the DCS. Maximum rate is constrained by the vapor return capacity of the vessel.
*   Initial Rate: Start at 500 cubic meters per hour for cooling down.
*   Full Rate: Ramp to 12,000 cubic meters per hour after thermal equilibrium.
*   Vapor Return: Maintain ship tank pressure between 10-15 kPag during unload.
*   Temperature Gradient: Pipe wall cooling rate must not exceed 10°C per minute.
*   Stop Sequence: Close ship valves before terminal valves to prevent trapping liquid.
"""  # noqa: E501

version = "0.0.1"
