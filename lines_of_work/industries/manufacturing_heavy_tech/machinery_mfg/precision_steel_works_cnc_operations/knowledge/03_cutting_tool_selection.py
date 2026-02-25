title = "Cutting Tool Selection and Geometry"

content = """
Selecting the appropriate cutting tool is fundamental to machining success.
Tool choice depends on material properties, operation type, surface finish
requirements, and machine capabilities.

**Tool Material Types:**
- **HSS (High-Speed Steel):** Cost-effective, tough, suitable for low-to-moderate
cutting speeds and complex tool geometries. Best for prototyping or soft materials.
- **Carbide (Tungsten Carbide):** High hardness, excellent heat resistance,
allows 3-10x faster cutting than HSS. Requires rigid setup due to brittleness.
- **Cermet:** Titanium carbide or carbonitride based, offers good wear resistance
and surface finish for finishing operations at medium speeds.
- **Ceramics:** Aluminum oxide or silicon nitride based, extreme heat resistance
for high-speed machining of cast iron and hardened steels.
- **PCD (Polycrystalline Diamond):** Superior for non-ferrous metals, abrasive
composites, and high-silicon aluminum. Not suitable for steel (carbon diffusion).
- **CBN (Cubic Boron Nitride):** Second hardest material, ideal for hard turning
(HRC 45+) and abrasive cast irons.

**End Mill Geometries:**
- **Number of Flutes:** 2-flute for soft materials and chip evacuation; 3-4 flute
for general purpose; 5+ flute for finishing and hard materials.
- **Helix Angle:** Low helix (30°) for roughing and rigid materials; high helix
(45°+) for finish cutting and improved surface finish.
- **Corner Radius:** Reduces chipping, improves tool life, creates stronger
cutting edge compared to sharp corners.
- **Ball End vs. Square End:** Ball end for 3D contouring and surface finishing;
square end for pockets, edges, and flat surfaces.

**Insert-Based Tools:**
Indexable inserts allow cutting edge replacement without tool disposal. Common
insert shapes include round (strongest), square (versatile), triangular (efficient),
and diamond (precision). Negative rake inserts are stronger; positive rake reduces
cutting forces.

**Coatings:**
TiN (gold, general purpose), TiAlN (dark gray, high temperature, ferrous),
AlTiN (harder variant for hard materials), TiCN (blue-gray, low friction), and
Diamond (non-ferrous only). Coatings extend tool life by reducing friction,
dissipating heat, and protecting from oxidation.
"""

version = "0.0.1"
