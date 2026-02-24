title: str = "Cloud Migration Strategies: The 6 Rs"

content: str = """
Cloud migration is the process of moving data, applications, and other 
business elements to a cloud computing environment. The "6 Rs" framework 
helps architects categorize and plan the migration of each workload.

**The 6 Rs of Migration:**
1. **Rehost (Lift-and-Shift):** Moving applications to the cloud without 
   making any changes. Fastest but least optimized for cloud benefits.
2. **Replatform (Lift-and-Reshape):** Making minor optimizations to 
   leverage cloud services (e.g., moving a self-hosted DB to a managed 
   service like Amazon RDS).
3. **Refactor / Rearchitect:** Reimagining how the application is 
   architected using cloud-native features like microservices or 
   serverless. Most effort but highest ROI.
4. **Repurchase:** Moving to a different product, typically a SaaS 
   platform (e.g., moving from on-premises CRM to Salesforce).
5. **Retire:** Identifying and decommissioning applications that are no 
   longer useful.
6. **Retain (Revisit):** Keeping applications on-premises for now, 
   possibly due to compliance or high migration complexity.

A successful migration requires a thorough discovery phase to map 
dependencies and select the appropriate "R" for every application in the 
portfolio.
"""

version: str = "0.0.1"
