title = "Eddy Current Testing (ET) for Surface Cracks"

content = """
Eddy Current Testing (ET) is an electromagnetic NDT method that detects surface and near-surface cracks, corrosion, and conductivity variations in electrically conductive materials. At Ridgecrest Metalworks, ET is used for surface crack detection in aluminum and non-ferrous components, sorting of mixed metal grades, and measurement of non-conductive coating thickness on aluminum.

The principle of ET is electromagnetic induction. An alternating current is passed through a coil (probe), generating an alternating magnetic field. When the probe is placed near a conductive material, this field induces circulating eddy currents in the material. These eddy currents create their own opposing magnetic field, which changes the electrical impedance of the coil. A crack or discontinuity interrupts the eddy current flow, causing a measurable change in coil impedance. The instrument displays the impedance change as a signal on a screen (impedance plane display).

Probe types and applications:
- Surface (pancake) probes: Flat coil held perpendicular to the surface; used for scanning flat surfaces for cracks and corrosion
- Encircling (ID/OD) coils: The part passes through or is surrounded by the coil; used for rapid inspection of rods, tubes, and fasteners in production
- Differential probes: Two coils in differential connection; sensitive to local changes but insensitive to gradual variations; ideal for crack detection while ignoring gradual conductivity changes

Test frequency selection: Lower frequencies penetrate deeper into the material (useful for sub-surface defects) but have lower sensitivity to fine surface cracks. Higher frequencies are confined to the surface layer (skin effect). Typical frequencies: 10 kHz–1 MHz for surface crack detection in aluminum; 200 Hz–10 kHz for tube inspection.

Calibration uses notched reference standards (artificial EDM notches of defined depth and length) machined in the same material type as the part. The instrument is calibrated to produce a defined screen response from the reference notch, and acceptance thresholds are set relative to this reference.

ET is fast, non-contact, and does not require coupling media (unlike UT). It is well suited to automated scanning of symmetrical parts. Limitations include inability to inspect through non-conductive coatings of variable thickness, sensitivity to lift-off variation (probe-to-surface gap), and limited penetration depth.
"""

version = "0.0.1"
