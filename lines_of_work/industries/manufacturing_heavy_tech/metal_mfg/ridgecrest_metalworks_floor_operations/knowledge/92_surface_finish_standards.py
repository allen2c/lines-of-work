title = "Surface Finish Standards and Measurement (Ra, Rz)"

content = """
Surface finish (surface texture or surface roughness) describes the microscopic geometric character of a machined surface—the lay, waviness, and roughness created by the machining process. Specifying and measuring surface finish is essential at Ridgecrest Metalworks because surface texture affects fatigue strength, sealing capability, bearing performance, friction, coating adhesion, and aesthetic appearance.

Surface finish parameters are defined in ASME B46.1 (US) and ISO 4287 (international). The most widely used parameter is Ra (arithmetic average roughness)—the average absolute deviation of the surface profile from the mean line over the measurement length. Ra is expressed in microinches (µin) in US practice or micrometers (µm) internationally (1 µin = 0.0254 µm). Common engineering surfaces range from Ra 250 µin (rough machining) to Ra 4 µin (precision grinding) to Ra 1 µin and below (honing, lapping).

Rz (average maximum height) represents the average of the five largest peak-to-valley heights within a measurement length. Rz is more sensitive to isolated high peaks or deep valleys than Ra and is preferred in European and automotive standards. Rz is approximately 4–7 times Ra for typical machined surfaces.

Rt (total profile height) is the maximum peak-to-valley height over the entire measurement length. Rp is the maximum peak height above the mean line. These parameters are used for specific applications like sealing surfaces.

The Rmax (or Rmax per ISO 4288) is the maximum single peak-to-valley height and is important for applications sensitive to the highest asperity.

Surface finish is measured with a contact profilometer (stylus instrument)—a diamond-tipped stylus traverses the surface and a transducer measures vertical displacement. The instrument calculates Ra, Rz, and other parameters electronically. Cutoff wavelength (λc, typically 0.8 mm for general machining) filters waviness from roughness.

Surface finish symbols on engineering drawings indicate the maximum Ra permitted. Operators must understand how to read these symbols and must check surface finish on the first piece and periodically during production using the shop profilometer. Visual/tactile comparator plates (roughness comparison specimens per ISO 2632) are used on the floor for quick checks between profilometer measurements.
"""

version = "0.0.1"
