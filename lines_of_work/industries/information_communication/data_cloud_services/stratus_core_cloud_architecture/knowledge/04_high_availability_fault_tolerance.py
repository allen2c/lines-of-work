title: str = "High Availability and Fault Tolerance Principles"

content: str = """
Resilience in the cloud is achieved through two primary concepts: High 
Availability (HA) and Fault Tolerance (FT). While often used 
interchangeably, they represent different levels of system robustness.

**High Availability (HA):** Refers to a system's ability to remain 
operational and accessible for a high percentage of time (e.g., 99.99% or 
"four nines"). HA is typically achieved through redundancy and automated 
failover. If one component fails, another takes its place, though there may 
be a brief period of degraded performance or a momentary interruption.

**Fault Tolerance (FT):** A higher standard where the system continues to 
operate without any interruption or data loss, even if a major component 
fails. FT requires total redundancy of hardware and state, often leading to 
significantly higher costs. It is reserved for mission-critical systems where 
even a few seconds of downtime is unacceptable.

**Key Architectural Patterns:**
1. **Multi-AZ Deployment:** Distributing resources across multiple isolated 
   Availability Zones within a region to protect against data center failures.
2. **Load Balancing:** Distributing incoming traffic across multiple 
   healthy instances to prevent any single instance from becoming a 
   bottleneck or single point of failure.
3. **Health Checks:** Continuously monitoring the status of resources and 
   automatically removing unhealthy ones from the rotation.

Architects must balance the cost of redundancy against the business impact 
of downtime to determine the appropriate resilience strategy.
"""

version: str = "0.0.1"
