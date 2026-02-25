title = "Dimensional Measurement and Quality Control"

content = """
Precision machining requires rigorous measurement to verify dimensional compliance
with engineering specifications. Understanding metrology tools and techniques
ensures quality output.

**Manual Measuring Instruments:**
- **Calipers (Vernier/Digital):** Measure OD, ID, depth, and step dimensions.
Typical resolution: 0.001" or 0.02mm. Suitable for general tolerances (±0.005").
- **Micrometers:** Higher precision than calipers (0.0001" or 0.001mm resolution).
Available for OD, ID, depth, and specialized applications (thread, groove, blade).
- **Height Gages:** Measure vertical dimensions from a reference surface.
Digital versions offer precision and data output capabilities.
- **Bore Gages:** Measure internal diameters with high precision. Telescoping
and dial bore gages provide comparative measurements; air gages offer non-contact
measurement for sensitive surfaces.

**Gauge Blocks and Standards:**
Precision-machined steel or ceramic blocks with certified dimensions. Used for
calibrating instruments, setting snap gages, and establishing reference heights.
Wrung combinations create precise stacks for any dimension.

**Coordinate Measuring Machines (CMM):**
Touch-probe or optical systems that measure 3D coordinates relative to a part
datum. CMMs provide comprehensive dimensional reports, geometric dimensioning and
tolerancing (GD&T) verification, and statistical process control data. Bridge-style,
gantry, and portable arm CMMs serve different application needs.

**Surface Finish Measurement:**
Profilometers measure Ra (arithmetic average), Rz (average peak-to-valley), and
other surface texture parameters. Critical for sealing surfaces, bearing seats,
and aesthetic requirements. Stylus-based and optical (white light interferometry)
methods available.

**Go/No-Go Gauging:**
Hard gauges with predefined limits verify acceptability without providing
measured values. Efficient for production inspection where tolerance bands are
well-established. Examples: plug gauges for holes, ring gauges for shafts,
thread gauges for threaded features.

**In-Process Inspection:**
On-machine probing uses spindle-mounted touch probes to verify part dimensions
before removing from the fixture. Allows machining compensation based on actual
measurements, improving accuracy and reducing scrap. Renishaw and Blum systems
integrate with modern CNC controls.

**Statistical Process Control (SPC):**
Charting measurement data (X-bar and R charts, Cp/Cpk calculations) monitors
process stability and capability. Trend detection enables preventive adjustments
before out-of-tolerance conditions occur. Cpk values above 1.33 indicate
capable processes; 1.67+ for critical features.
"""

version = "0.0.1"
