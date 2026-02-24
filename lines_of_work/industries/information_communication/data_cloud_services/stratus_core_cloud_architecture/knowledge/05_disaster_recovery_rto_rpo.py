title: str = "Disaster Recovery Strategies: RTO and RPO"

content: str = """
Disaster Recovery (DR) is the process of restoring IT systems and data after 
a catastrophic event. A robust DR plan is defined by two key metrics: 
Recovery Time Objective (RTO) and Recovery Point Objective (RPO).

**Recovery Time Objective (RTO):** The maximum acceptable duration of 
downtime after a disaster occurs. It answers the question: "How long can we 
afford to be offline?"

**Recovery Point Objective (RPO):** The maximum acceptable amount of data 
loss measured in time. It answers the question: "How much data can we afford 
to lose?" (e.g., an RPO of 1 hour means the system must be restorable to a 
state no older than 1 hour).

**Common DR Patterns:**
1. **Backup and Restore:** Low cost, high RTO/RPO. Data is backed up to 
   cloud storage and restored manually or via scripts when needed.
2. **Pilot Light:** A minimal version of the environment is kept running 
   (e.g., just the database with data replication). In a disaster, the rest 
   of the infrastructure is provisioned quickly.
3. **Warm Standby:** A scaled-down but fully functional version of the 
   environment is always running. Failover is faster than Pilot Light.
4. **Multi-Site (Active-Active):** The full environment is running in two 
   or more regions simultaneously. Traffic is shifted immediately in case of 
   a regional failure. This offers the lowest RTO/RPO but the highest cost.

The choice of DR strategy is a trade-off between the cost of the 
infrastructure and the potential financial loss resulting from downtime or 
data corruption.
"""

version: str = "0.0.1"
