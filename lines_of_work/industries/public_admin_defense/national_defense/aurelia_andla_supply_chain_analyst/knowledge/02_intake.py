title = "Requisition Intake & Validation"

content = """
- Requisitions arrive via MILSTRIP DLA Transaction Services; the analyst verifies document number format (A0xx series for materiel), routing identifier (RIC), and priority designator.
- Validate against the 14-character NSN: FSC (4) + NIIN (9) + reference code (1). Reject any record where NIIN does not match the published FLIS record as of the query date.
- Suspense rules: priority 01–03 should be actioned within 5 business days; 04–08 within 15; 09 (stock) within 30. Any requisition past suspense is added to the Daily Supply Exception report.
- Common rejection causes to surface: missing unit price, duplicate document number, closed-out DoDAAC, item suspended (SCC "H" or "J").
- When a requisition references a partial NSN or local stock number, route to the LSN/NSN cross-reference queue; do not auto-translate.
"""  # noqa: E501

version = "0.0.1"
