title = "Photolithography Fundamentals and Optical Resolution"

content = """
Photolithography is the core process of semiconductor manufacturing, using light 
to transfer a circuit pattern from a photomask to a light-sensitive chemical 
photoresist on a silicon wafer. The resolution of this process is governed by 
Rayleigh's criterion, which defines the minimum resolvable feature size (CD).

**Rayleigh's Criterion:**
The critical dimension (CD) is calculated as CD = k1 * λ / NA, where:
- λ (lambda) is the wavelength of the light source (e.g., 193nm for ArF DUV, 
  13.5nm for EUV).
- NA (Numerical Aperture) is the light-gathering capacity of the lens system.
- k1 is a process-dependent factor reflecting the complexity and optimization 
  of the lithography system.

**Resolution Enhancement:**
To push resolution beyond the diffraction limit, several techniques are used:
- **Numerical Aperture (NA) Increase:** Larger lenses or immersion lithography 
  (using water between the lens and wafer) increase NA.
- **Wavelength Reduction:** Shifting from DUV (193nm) to EUV (13.5nm) provides 
  a massive jump in resolution.
- **k1 Reduction:** Advanced techniques like Optical Proximity Correction (OPC), 
  Phase Shift Masks (PSM), and Off-Axis Illumination (OAI) lower the k1 factor.

**Process Latitude:**
Achieving high resolution is only half the battle; the process must also have 
sufficient latitude (Depth of Focus and Exposure Latitude) to be manufacturable 
at scale. A narrow process window leads to poor yield and high defectivity.
"""

version = "0.0.1"
