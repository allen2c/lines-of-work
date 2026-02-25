title = "Surface Roughness Profilometers: Operation and Calibration"

content = """
Surface roughness profilometers are instruments that quantitatively measure the texture of machined and finished surfaces. At Ridgecrest Metalworks, profilometers are used to verify that machined surfaces meet the roughness specifications on engineering drawings and to confirm that prepared surfaces are suitable for coating.

Contact (stylus) profilometers are the most common type on the production floor. The instrument draws a fine diamond stylus across the surface at a controlled traverse speed. The stylus rides in the surface valleys and peaks; vertical displacement is converted to an electrical signal by an LVDT or piezoelectric transducer. The instrument's electronics apply digital filters, calculate roughness parameters (Ra, Rz, Rt, Rq, etc.), and display results on a screen or printout.

Key operating parameters:
- Evaluation length (ln): The total length over which roughness is assessed. Per ISO 4288, typically five cut-off wavelengths (5 × λc). For Ra 0.8–6.3 µm, λc = 0.8 mm, ln = 4.0 mm is standard.
- Cut-off wavelength (λc): The filter separating roughness from waviness. Correct selection is essential; using too short a cut-off on a wavy surface reads low roughness. ISO 4288 defines cut-off selection based on expected Ra range.
- Stylus tip radius: Standard 2 µm radius resolves features down to approximately 1–2 µm wide. Coarser 5 µm styli are less likely to be damaged but miss very fine features.
- Traverse speed: Manufacturer-specified; too fast causes filtering errors.

Operating procedure:
1. Clean the surface; remove chips, coolant, and oil with a clean cloth or solvent wipe. Contamination on the surface causes false peaks and inflated roughness readings.
2. Place the instrument on the surface with the stylus perpendicular to the machining lay direction (for turned surfaces, measure along the axis; for milled surfaces, measure across the cutter path).
3. Select correct λc and evaluation length. Start measurement.
4. Record all parameters and readings on the inspection record.

Calibration: The profilometer is calibrated before each session using a certified roughness reference specimen (traceable to national standards). If the measured value of the reference is outside the instrument's specified accuracy band (typically ±10 % of the reference value), the instrument is removed from service and sent for service. Reference specimens are also recertified periodically by an accredited laboratory.
"""

version = "0.0.1"
