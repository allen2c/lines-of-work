title = "Office Supply Inventory Management"

content = """
- Maintain a digital inventory spreadsheet (Google Sheets) of all office supplies: categories (paper, pens, folders, toner, coffee, cleaning supplies, etc.).
- Each item has a minimum stock level (e.g., copy paper: min 10 reams, max 50 reams; black pens: min 20, max 100).
- Perform a physical count every Monday morning at 9:00 AM. Update the spreadsheet.
- When any item falls below its minimum, add it to the weekly order list. The order list is finalized on Tuesday at 10:00 AM.
- For high-usage items (coffee, paper towels), set a reorder point at 20% of max. For low-usage items (binders, staplers), reorder only when stock reaches zero.
- Flag any sudden drop in inventory (e.g., missing items) to the office manager.
"""

version = "0.0.1"
