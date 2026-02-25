title = "Cutting Speeds, Feeds, and Depth of Cut"

content = """
Cutting speed, feed rate, and depth of cut are the three fundamental machining parameters that determine material removal rate, surface finish, tool life, and machining forces. At Ridgecrest Metalworks, process engineers establish starting parameters for each operation, which operators are expected to apply and adjust within defined limits.

Cutting speed (V) is the velocity at which the tool cutting edge moves relative to the workpiece surface, expressed in surface feet per minute (SFM) or meters per minute (m/min). For turning and boring, the required spindle RPM is calculated as: RPM = (SFM × 12) / (π × diameter) in imperial units. Cutting speed recommendations are published by tool manufacturers and are based on tool material, workpiece material, and desired tool life. For example, carbide turning of mild steel (AISI 1020) typically uses 400–700 SFM for roughing, 600–900 SFM for finishing. Hard materials require lower speeds; soft non-ferrous metals (aluminum, brass) allow very high speeds (800–3,000 SFM with carbide).

Feed rate is the rate of tool advance per unit time (in/min for milling; in/rev for turning). In milling, feed per tooth (chip load) is the primary parameter: recommended chip loads for carbide end mills range from 0.001–0.006 in/tooth for steel, depending on diameter and depth of cut. Too light a chip load causes rubbing rather than cutting, generating excessive heat and accelerating wear. Too heavy a chip load causes chipping of the cutting edge.

Depth of cut (DOC) is the amount of material removed in one pass—measured radially in turning and axially or radially in milling. Roughing passes use heavier DOC (0.050–0.250 inch) with moderate feeds; finishing passes use light DOC (0.005–0.020 inch) to minimize deflection and thermal effects, achieving dimensional accuracy and fine finish.

Taylor's Tool Life equation (V × T^n = C) describes the inverse relationship between cutting speed and tool life: doubling cutting speed may reduce tool life by 80% or more. Operators should follow recommended speeds; arbitrarily increasing speed to meet cycle time targets at the expense of tool life is counterproductive. Monitoring tool life and replacing worn inserts at the prescribed interval prevents scrapped parts from dimension drift and surface damage.
"""

version = "0.0.1"
