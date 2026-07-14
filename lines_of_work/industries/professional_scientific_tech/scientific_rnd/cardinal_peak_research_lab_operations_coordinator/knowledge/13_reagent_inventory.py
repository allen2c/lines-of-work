title = "Reagent and Consumable Inventory"

content = """
- Maintain a live inventory of reagents, solvents, standards, and consumables with
  quantity on hand, lot number, receipt date, expiration date, storage location, and
  minimum reorder level.
- Apply first-expiry-first-out (FEFO): issue the stock that expires soonest first to
  minimize waste, and remove expired materials from active shelves promptly.
- Track lot numbers of reference standards and critical reagents against the studies that
  used them, so a recalled or failed lot can be traced to affected work.
- Set reorder points based on lead time and usage rate; reorder before hitting minimum so
  a critical reagent never stops a scheduled run. Account for long lead times on
  specialty items and controlled substances.
- Log the preparation of working solutions: preparer, date, components and lots,
  concentration, assigned expiry, and a unique solution ID. Prepared reagents get labels
  as rigorous as purchased ones.
- Reconcile physical counts against the system periodically (cycle counts) to catch
  shrinkage, mislabeling, and unlogged usage before they cause a stockout or a data
  question.
"""

version = "0.0.1"
