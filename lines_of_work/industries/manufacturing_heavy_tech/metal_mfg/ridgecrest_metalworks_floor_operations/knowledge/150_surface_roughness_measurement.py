title = "Surface Roughness Measurement and Acceptance Criteria"

content = """
Surface roughness measurement quantifies the texture of a machined or finished surface. At Ridgecrest Metalworks, surface roughness is specified on engineering drawings and must be verified before parts proceed to coating or assembly. Understanding roughness parameters and how to measure them correctly is essential for production and quality personnel.

The most commonly used roughness parameter is Ra (arithmetic mean roughness), which is the average deviation of the surface profile from its mean line over the evaluation length. Ra is expressed in micrometers (µm) or microinches (µin). Other important parameters include:
- Rz (ten-point mean roughness / maximum height): Average of the five highest peaks and five deepest valleys; more sensitive to isolated defects than Ra
- Rt (total roughness height): Maximum peak-to-valley height over the entire measurement length
- Rq (root mean square roughness): Statistical RMS of profile deviations; slightly higher than Ra for typical profiles

Contact profilometers use a diamond stylus dragged across the surface at controlled speed. The stylus tip radius (typically 2 µm or 5 µm) limits the minimum feature detectable. The instrument digitizes the profile and calculates roughness parameters after applying a Gaussian cut-off filter (lambda-c) that separates roughness from waviness. Selecting the correct cut-off wavelength for the expected roughness is important; ISO 4288 provides guidance based on the expected Ra range.

Non-contact profilometers (optical: white light interferometry, confocal, or focus variation) measure surface texture without stylus contact, which is important for soft metals, thin coatings, or delicate finishes. These methods also provide 3D areal surface texture (Sa, Sz) per ISO 25178.

Typical roughness acceptance criteria at Ridgecrest:
- Turned surfaces, functional bores: Ra 1.6 µm (63 µin)
- Ground surfaces, bearing seats: Ra 0.8 µm (32 µin) or 0.4 µm (16 µin)
- Lapped or honed surfaces: Ra 0.2–0.4 µm (8–16 µin)
- Sand cast surfaces (as-cast): Ra 12.5 µm (500 µin) typical
- Grit-blasted surfaces prior to coating: Rz 40–75 µm

Profilometers are calibrated using certified reference standards traceable to national measurement institutes. Calibration records are maintained and instruments are recalibrated at defined intervals (typically every 12 months or after impact damage).
"""

version = "0.0.1"
