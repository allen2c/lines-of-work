title = "Order Picking Methods and Strategies"

content = """
Order picking is the most labor-intensive operation in the warehouse. Meridian
Fulfillment Center employs multiple picking strategies optimized for different
order profiles and service requirements.

**Discrete Order Picking:** One picker completes an entire order from start to
finish. This method suits large, multi-tote orders or orders containing fragile
items requiring careful handling. It minimizes consolidation errors but may
result in longer travel times for geographically dispersed SKUs.

**Batch Picking:** Multiple orders are grouped into a single picking task. The
picker travels the warehouse once, collecting all items for the batch, then
sorts them to individual orders at a consolidation point. Ideal for small,
single-line orders with high velocity. Reduces travel time significantly.

**Zone Picking:** The warehouse is divided into zones, each staffed by dedicated
pickers. Orders pass through zones sequentially, with each picker adding their
zone's items. Complex orders are split across zones and consolidated downstream.
Enables parallel processing and picker specialization by product type.

**Wave Picking:** Orders are released in scheduled waves based on carrier cutoff
times, service levels, or destination. A wave may use any picking method. Waves
allow workload balancing across shifts and ensure time-sensitive orders meet
their shipping deadlines.

**Pick-to-Cart, Pick-to-Tote, Pick-to-Pallet:** The pick destination varies by
order size. Small e-commerce orders go to totes on carts. Large B2B orders may
pick directly to pallets. The WMS directs the appropriate container type for
each pick task, optimizing downstream handling.
"""

version = "0.0.1"
