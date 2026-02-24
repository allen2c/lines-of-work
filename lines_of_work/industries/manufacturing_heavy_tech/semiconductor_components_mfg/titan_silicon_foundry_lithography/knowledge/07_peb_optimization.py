title = "Post-Exposure Bake (PEB) Optimization"

content = """
The Post-Exposure Bake (PEB) is a critical step in the chemically amplified 
resist (CAR) process. It occurs after the wafer is exposed in the scanner 
but before it is developed.

**Acid Diffusion Control:**
During PEB, the acid generated during exposure diffuses through the resist 
and catalyzes the chemical reaction that changes its solubility. The 
temperature and duration of the bake must be precisely controlled to 
manage this diffusion. Too much diffusion leads to blurred patterns and 
loss of resolution; too little leads to incomplete reactions and poor 
sensitivity.

**Temperature Uniformity:**
The PEB hotplate must have exceptional temperature uniformity (often better 
than 0.1°C) across the entire 300mm wafer. Even slight temperature 
gradients can cause significant CD variations across the wafer. Modern 
hotplates use multi-zone heating and active cooling to achieve this.

**PEB Sensitivity:**
Different resist chemistries have different "PEB sensitivities," which 
is the change in CD per degree of bake temperature. Minimizing this 
sensitivity is a key goal in resist design, as it makes the process 
more robust to small temperature fluctuations.
"""

version = "0.0.1"
