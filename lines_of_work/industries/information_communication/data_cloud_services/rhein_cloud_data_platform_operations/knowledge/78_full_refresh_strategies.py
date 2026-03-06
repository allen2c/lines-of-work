title = "Full Refresh Strategies"

content = """
Full refresh reloads all data from source. Used when incremental logic is
unreliable, after major corrections, or for small tables. Full refresh is
expensive; schedule during maintenance windows. Consider truncate-and-load
vs delete-and-insert. Ensure target is unavailable for queries during refresh
or use swap tables to minimize downtime.
"""

version = "0.0.1"
