title = "Lot and Batch Traceability on the Production Floor"

content = """
Traceability is the ability to reconstruct the full history of a part: which raw material (from which mill heat) was used, which machines processed it, which operators worked on it, which inspection steps it passed, and which customer shipment it went out in. Traceability is a contractual requirement for most of Ridgecrest Metalworks' customers and is mandated by ISO 9001 clause 8.5.2.

**Lot control concept.** A lot is a defined quantity of material or parts manufactured under the same conditions from the same material heat, in the same production run. All parts in a lot share traceability to a single set of records. Mixing parts from different lots without documentation creates a traceability break—a serious audit finding.

**Heat number traceability.** Every piece of steel or aluminum used in production must have its mill heat number recorded on the shop traveler. When material is received, the heat number is on the MTR and on the material label. When material is issued to a work order, the issuing transaction in SAP captures the lot/heat number. The traveler records it manually as a second verification.

**Part marking.** Finished parts that require individual traceability are permanently marked with:
- Part number and revision
- Work order or lot number
- Heat number (for raw material traceability)
- Date code (year/week or month/year)
Methods include: laser engraving, electro-chemical etching, stamping, paint stencil, or barcode label—specified by the drawing or customer spec. Marks must be placed in the location specified on the drawing and must remain legible through the service life of the part.

**Splitting and merging lots.** If a lot is split into subgroups (e.g., for separate shipping releases), each subgroup retains the original lot number with a suffix. Merging two separate lots into one shipment is not permitted unless both lots are traceable and the customer consents.

**Traceability failure response.** If traceability is broken—material label missing, heat number not on traveler, lot records lost—the affected material is quarantined immediately. QA conducts an investigation to re-establish identity through remaining records. If identity cannot be confirmed, the material is treated as non-conforming until full re-verification is complete.

Traceability records must be retained for the same period as other quality records.
"""

version = "0.0.1"
