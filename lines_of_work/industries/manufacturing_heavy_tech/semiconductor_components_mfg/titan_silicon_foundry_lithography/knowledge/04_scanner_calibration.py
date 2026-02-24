title = "Scanner Calibration and Focal Plane Stability"

content = """
The lithography scanner is the most complex machine in the fab, requiring 
constant calibration to maintain nanometer-scale precision. Focal plane 
stability is paramount, as even a few nanometers of drift can cause pattern 
blurring or failure.

**Autofocus Systems:**
Scanners use high-precision sensors to map the wafer's topography in real-time 
during exposure. This "leveling" process ensures the wafer surface stays 
within the scanner's Depth of Focus (DoF). Any deviation in the wafer's 
flatness or the sensor's calibration can lead to "focus spots."

**Lens Heating and Compensation:**
As the scanner operates, the high-energy light source heats the optics, causing 
slight changes in their shape and refractive index. Scanners use active 
compensation systems, such as deformable mirrors or gas-pressure adjustments, 
to correct for these thermal aberrations in real-time.

**Stage Metrology:**
The wafer stage must move with sub-nanometer accuracy. Laser interferometers 
and encoders track the stage's position at all times. Calibration routines 
regularly check for stage "grid" errors, ensuring that the scanner's 
coordinate system remains stable over time.
"""

version = "0.0.1"
