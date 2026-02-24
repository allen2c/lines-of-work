title = "Speeds, Feeds, and Machining Parameters"

content = """
Speeds and feeds determine cutting efficiency, tool life, surface finish, and
chip formation. Proper calculation balances material removal rate against
tool wear and part quality.

**Surface Feet Per Minute (SFM):**
SFM represents the cutting speed at the tool's periphery. It is calculated as:
SFM = (RPM × π × Tool Diameter) / 12 (for inches) or directly in metric.
Recommended SFM varies by tool material and workpiece material. Example: Carbide
end mill in mild steel: 400-600 SFM; HSS in same material: 80-120 SFM.

**Spindle Speed (RPM) Calculation:**
RPM = (SFM × 12) / (π × Tool Diameter) for imperial units.
RPM = (SFM × 1000) / (π × Tool Diameter) for metric units.
Always consult manufacturer recommendations and adjust based on machine rigidity.

**Feed Rate Calculation:**
Feed Rate (IPM or mm/min) = RPM × Chip Load per Tooth × Number of Flutes.
Chip load (IPT or mm/tooth) depends on tool diameter, material, and operation type.
Typical chip loads range from 0.001" (fine finishing) to 0.020" (heavy roughing).

**Depth of Cut (DOC) and Width of Cut (WOC):**
- **Radial Engagement (WOC):** Slotting uses 100% tool diameter; high-efficiency
milling uses 5-15% for optimal chip thinning.
- **Axial Engagement (DOC):** End milling typically uses 1-2x tool diameter;
face milling varies by insert and application. Deeper cuts require reduced speeds/feeds.

**Chip Thinning:**
When radial engagement is less than 50% of tool diameter, chips become thinner
than the programmed feed per tooth. Increase feed rates by 1/(sin(arccos(1-2×ae/D)))
to maintain proper chip load and avoid rubbing.

**Adaptive Clearing and High-Speed Machining:**
Constant tool load strategies maintain consistent engagement angles, allowing
aggressive parameters without shock loading. Toolpaths follow trochoidal or
corner-rolling patterns to preserve consistent chip formation throughout the cut.

**Trochoidal Milling:**
A technique using small radial stepovers with continuous motion, allowing full
depth cuts with small tools. Reduces tool deflection and extends tool life
in deep pocket machining.
"""

version = "0.0.1"
