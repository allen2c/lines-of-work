title = "Reading Engineering Drawings and Specifications"

content = """
Engineering drawings are the authoritative technical description of the part Ridgecrest Metalworks is contracted to produce. Every operator who sets up a machine, runs a process, or inspects a part must be able to read the relevant sections of the applicable drawing. Misreading or ignoring drawing information is a root cause of nonconforming parts and customer escapes.

**Drawing title block.** The title block (typically bottom right) contains:
- Part name and number.
- Revision level (letter or number—always confirm you have the current revision).
- Drawing scale and sheet number.
- Material specification.
- Tolerances (general tolerance note—applies to all dimensions without individual tolerances specified).
- Customer name and any customer part number.
- Release and approval signatures.
- Proprietary/distribution restrictions.

**Dimensioning conventions.** Ridgecrest receives drawings in both first-angle (European/ISO) and third-angle (US/ASME) projection. The projection symbol (a truncated cone graphic) in the title block identifies which convention applies. Confusing projection angles inverts views and causes incorrect machining.

**Geometric Dimensioning and Tolerancing (GD&T).** Most precision drawings use GD&T symbols per ASME Y14.5:
- Position (locates features within a tolerance zone relative to a datum).
- Flatness, straightness (form controls).
- Perpendicularity, parallelism, angularity (orientation controls).
- Concentricity, runout, total runout (for turned parts and shafts).
- Profile of a line/surface (for complex contours).

Operators working on drawings with GD&T must understand the datum reference frame (which surfaces establish the coordinate system) because the part must be fixtured relative to the correct datums for any GD&T requirement to be meaningful.

**Surface finish callouts.** Ra (arithmetic mean roughness) in microinches or micrometers is specified on machined surfaces. Common values at Ridgecrest: 63 Ra for general machined surfaces, 32 Ra for sliding contact surfaces, 16 or 8 Ra for sealing surfaces. Grinding or honing is typically required to achieve Ra below 32.

**Weld symbols.** AWS A2.4 weld symbols specify: weld type (fillet, groove, plug), weld size, weld length, and whether the weld is all around or on the arrow side only. The field weld symbol and all-around symbol have specific meanings that affect how the joint is prepared and completed.

**Drawing notes.** General notes (in the notes section) apply to the entire drawing unless modified by a local note. Always read all notes before setting up—special process requirements, inspection requirements, and prohibited materials are often in the notes section.
"""

version = "0.0.1"
