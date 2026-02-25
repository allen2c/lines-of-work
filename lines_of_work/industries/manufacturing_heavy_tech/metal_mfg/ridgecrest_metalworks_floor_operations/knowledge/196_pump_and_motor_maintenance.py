title = "Pump and Electric Motor Maintenance"

content = """
Electric motors and pumps are ubiquitous throughout Ridgecrest Metalworks, driving coolant pumps, hydraulic power units, conveyor drives, fans, and compressed air systems. Reliable motor and pump operation is critical to production continuity.

Electric motor maintenance:

Routine checks (monthly): Measure motor operating temperature using an infrared thermometer at the bearing housings and motor frame. Overheating above the motor's rated ambient class indicates overloading, poor ventilation, bearing deterioration, or voltage imbalance. Check motor supply voltage (all three phases for three-phase motors); voltage imbalance exceeding 2 % causes significant heating in the windings. Listen for unusual noise (bearing roughness, resonance).

Periodic maintenance (annually or per vibration analysis trigger):
- Motor bearings: Relubricate anti-friction bearings per the manufacturer's specification (quantity and type are critical; over-greasing causes as much damage as under-greasing). Replace bearings when vibration analysis indicates defect or when scheduled replacement interval is reached (typically 3–5 years for standard motors in clean environments; more frequently in dirty or wet environments).
- Insulation resistance test (megger test): Measure winding insulation resistance to ground with a 500 V or 1000 V DC insulation resistance tester. Compare to the motor's previous readings and to the minimum acceptable value per IEEE 43 (1 MΩ per kV of rated voltage as an absolute minimum; > 100 MΩ for healthy windings). Declining insulation resistance indicates moisture ingress or insulation degradation; the motor should be investigated and dried or rewound.
- Terminal box: Inspect for moisture, corrosion, and cable gland integrity.

Pump maintenance:

Centrifugal pumps: Check mechanical seal condition for leaks; a weeping seal can be monitored, but active leaking requires replacement. Check impeller clearance on seals that provide adjustment. Inspect couplings for alignment and coupling element wear.

Positive displacement pumps (gear pumps, vane pumps): Check for reduced flow or rising case temperature, which indicate internal wear (increased internal leakage). Replace pump or internal components when volumetric efficiency falls below specification. Maintain correct inlet conditions (strainer clean, no air ingestion) to prevent cavitation damage.

Pump and motor alignment: Misalignment is a primary cause of premature bearing and seal failure. Alignment is checked after any installation or bearing replacement using laser alignment tools. Acceptable residual misalignment is typically < 0.05 mm parallel and < 0.05 mrad angular at the coupling for standard motors.
"""

version = "0.0.1"
