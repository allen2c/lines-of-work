title = "Dispatch Scheduling"

content = """
Dispatch scheduling allocates vehicles and drivers to consignments so that pickups and
deliveries are met within agreed windows while respecting driver hours and vehicle
availability.

**Inputs:** Consignment details (origin, destination, weight, volume, special handling),
requested date and time, and customer priority. Match with available trucks and drivers
and consider existing commitments and maintenance.

**Outputs:** A clear assignment: vehicle, driver, loading time and location, and
expected delivery. Communicate to the driver in Hindi (or their working language) and
confirm understanding. Update the customer or TMS with the planned schedule.

**Revisions:** When delays or breakdowns occur, reschedule or reassign as needed and
inform affected parties. Avoid overloading drivers or asking them to exceed rest limits.
"""  # noqa: E501

version = "0.0.1"
