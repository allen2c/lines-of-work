title = "Critical Dimension (CD) Uniformity"

content = """
Critical Dimension (CD) refers to the width of the smallest features in a 
circuit pattern, such as a transistor gate or a contact hole. Maintaining 
CD uniformity (CDU) across the entire wafer and from wafer-to-wafer is 
essential for device performance and yield.

**CD-SEM Metrology:**
Critical dimensions are measured using a specialized Scanning Electron 
Microscope (CD-SEM). Unlike optical microscopes, CD-SEMs use electron 
beams to achieve the resolution needed to measure features only a few 
nanometers wide. CDU is typically reported as a 3-sigma variation.

**Dose and Focus Effects:**
CD is primarily controlled by the exposure dose (energy) and the focus 
offset. A higher dose typically results in smaller features for positive 
resists. The relationship between dose, focus, and CD is mapped using 
"Bossung curves," which help engineers find the optimal "process window" 
where CD is least sensitive to focus variations.

**Etch Bias:**
The CD measured after lithography (ADI - After Develop Inspection) is 
often different from the CD after the subsequent etching step (AEI - 
After Etch Inspection). This "etch bias" must be characterized and 
accounted for during the lithography process setup.
"""

version = "0.0.1"
