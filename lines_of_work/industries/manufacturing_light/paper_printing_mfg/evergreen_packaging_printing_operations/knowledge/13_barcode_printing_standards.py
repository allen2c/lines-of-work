"""
Knowledge about barcode printing standards for packaging applications.
"""

title = "Barcode Printing Standards"

content = """
Barcodes enable automated identification throughout the supply chain.
Print quality directly impacts scanning reliability, making adherence to
standards essential for packaging operations.

**Symbology Types:** UPC-A and EAN-13 serve retail point-of-sale with
fixed-length numeric encoding. Code 128 accommodates variable-length
alphanumeric data for logistics. GS1-128 applies standard identifiers
(SSCC, GTIN, dates) to shipping containers. QR Code and Data Matrix enable
2D scanning with high data density for consumer engagement and traceability.

**GS1 Standards:** The GS1 system provides globally unique identification.
GTINs (Global Trade Item Numbers) identify products. SSCCs (Serial Shipping
Container Codes) identify logistics units. Application Identifiers (AI)
qualify data meaning (batch, expiration, quantity). Proper encoding ensures
interoperability across trading partners.

**Print Quality Grading:** ISO/IEC 15415 and 15416 define verification
parameters. Scan grades (A, B, C, D, F) reflect decodability, symbol contrast,
minimum reflectance, edge determination, and other factors. Grade C or
better typically represents acceptable quality. Verifiers measure these
parameters with calibrated aperture and wavelength settings.

**Packaging Considerations:** Barcode position affects scanning efficiency.
The Quiet Zone (clear margin) must surround the symbol. Reflectance contrast
between bars and spaces must meet minimums — challenging on brown corrugated
or printed backgrounds. Color selection impacts readability: dark bars on light
backgrounds scan reliably; blue, green, and brown bars may not scan if too
light.

**Common Defects:** Bar gain/loss occurs when bars print wider or narrower
than specified, affecting decodability. Void spots within bars break continuity.
Spreading inks create connected bars. Poor substrate reflectance reduces
contrast. Each defect type requires process adjustments: ink viscosity,
pressure settings, or substrate specification changes.
"""

version = "0.0.1"
