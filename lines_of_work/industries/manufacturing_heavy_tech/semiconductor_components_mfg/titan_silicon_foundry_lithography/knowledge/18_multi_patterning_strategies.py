title = "Multi-Patterning Strategies (LELE, SADP)"

content = """
Multi-patterning is a technique used to extend the resolution of 
optical lithography beyond its single-exposure limit. It involves 
splitting a single circuit layer into multiple exposures.

**LELE (Litho-Etch-Litho-Etch):**
LELE is a straightforward multi-patterning technique where half 
of the pattern is exposed and etched, followed by the second 
half. This effectively doubles the pattern density but 
requires precise overlay between the two exposures.

**SADP (Self-Aligned Double Patterning):**
SADP is a more complex technique that uses a "spacer" process 
to double the pattern density. A "mandrel" pattern is first 
formed, and then a thin film (the spacer) is deposited and 
etched to leave only the sidewalls. The mandrels are then 
removed, leaving behind a pattern with twice the density 
of the original. SADP is less sensitive to overlay errors 
than LELE.

**SAQP (Self-Aligned Quadruple Patterning):**
SAQP is an extension of SADP, using two spacer steps to 
quadruple the pattern density. This technique is used for 
the most critical layers in advanced logic and memory 
devices.

**Design Rule Constraints:**
Multi-patterning introduces complex design rules, as the 
original circuit layout must be "colored" (split into multiple 
masks) in a way that is manufacturable.
"""

version = "0.0.1"
