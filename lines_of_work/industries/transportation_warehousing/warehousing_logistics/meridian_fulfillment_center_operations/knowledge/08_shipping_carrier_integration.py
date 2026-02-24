title = "Shipping Carrier Integration and Manifesting"

content = """
Seamless carrier integration ensures that orders flow from packing to the
correct transportation mode with accurate documentation and tracking.

**Carrier Selection:** The WMS applies business rules to select the optimal
carrier for each shipment. Rules consider service level (ground, express),
destination zone, weight, dimensions, and special handling requirements.
High-value shipments may require signature confirmation. Perishables need
time-definite delivery.

**Manifest Generation:** As packages complete packing, they are scanned to
carrier manifests. The manifest is the legal document transferring custody
to the carrier. It includes package count, total weight, and tracking numbers.
Carriers require manifests before trailer departure.

**Label Compliance:** Each carrier has specific label format requirements.
The WMS generates compliant labels with proper barcodes, routing codes, and
service indicators. Non-compliant labels may be rejected by carrier sortation
systems, causing delays or mis-shipments.

**Trailer Loading:** Packages are loaded by destination or delivery route
to facilitate efficient unloading. Floor-loaded trailers require proper
bracing to prevent shifting in transit. Palletized freight is secured with
stretch wrap and banding. Loading accuracy is verified by scanning outbound
shipments.

**Tracking and Confirmation:** Upon carrier pickup, the WMS receives
confirmation and tracking numbers. Customers are notified of shipment with
tracking links. The system monitors for delivery exceptions and updates
order status upon confirmed delivery. POD (Proof of Delivery) images are
retrieved for high-value shipments.
"""

version = "0.0.1"
