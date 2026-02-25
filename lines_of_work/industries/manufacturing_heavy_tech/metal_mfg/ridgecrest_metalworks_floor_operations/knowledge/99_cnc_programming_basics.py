title = "CNC Programming Basics for Floor Operators"

content = """
CNC (Computer Numerical Control) machine tools execute machining operations by following a set of programmed instructions (G-code) that specify tool motion, spindle speed, feed rate, and auxiliary functions. At Ridgecrest Metalworks, floor operators are expected to understand basic CNC program structure, read programs to verify operations, make approved parameter edits, and recognize program errors before they cause crashes or scrap.

G-code programs are structured as blocks (lines), each containing one or more words (a letter address followed by a numerical value). Common G-code addresses: G00 (rapid positioning), G01 (linear feed motion), G02/G03 (circular arc motion, clockwise/counterclockwise), G17/18/19 (plane selection), G41/G42 (cutter diameter compensation left/right), G43 (tool length offset apply), G73/G83 (drilling cycles), G90/G91 (absolute/incremental positioning mode), G94/G95 (feed per minute/per revolution). M-codes are miscellaneous functions: M03/M04 (spindle on CW/CCW), M05 (spindle off), M06 (tool change), M08/M09 (coolant on/off), M30 (program end).

Tool offsets are critical: tool length offsets (H offsets in Fanuc convention) compensate for individual tool length differences so programmed Z coordinates correspond to actual tool tip positions. Cutter radius compensation (D offset) adjusts the tool path laterally by the actual tool radius, allowing use of a slightly undersized tool or compensation for tool wear without reprogram.

Before running any new program or restarted job, operators must: verify the correct program number and revision is loaded, check all tool offsets match the actual tools in the spindle, verify workpiece zero (datum) is set correctly by probing or gauge block verification, perform a dry run (single-block, feed-hold ready) at reduced feedrate override to verify tool paths visually before full-speed production.

Operators make approved edits for: adjusting feed rate or speed overrides within documented limits, changing tool life counters, and entering dimensional offset changes after measurement. Program content changes beyond approved limits require engineering authorization. All unauthorized changes to program files are prohibited and may result in product nonconformance and disciplinary action.
"""

version = "0.0.1"
