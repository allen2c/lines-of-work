title: str = "Cloud Data Persistence: SQL vs. NoSQL"

content: str = """
Choosing the right data persistence layer is a critical architectural 
decision that impacts performance, scalability, and data integrity. The 
primary choice is often between Relational (SQL) and Non-Relational (NoSQL) 
databases.

**Relational Databases (SQL):**
*   **Characteristics:** Structured schema, ACID compliance (Atomicity, 
    Consistency, Isolation, Durability), and powerful JOIN capabilities.
*   **Use Cases:** Complex queries, financial transactions, and 
    applications where data consistency is paramount. Examples include 
    Amazon RDS (PostgreSQL, MySQL) and Azure SQL Database.
*   **Scaling:** Primarily vertical (increasing CPU/RAM), though read 
    replicas can provide some horizontal read scaling.

**Non-Relational Databases (NoSQL):**
*   **Characteristics:** Flexible schema (Document, Key-Value, Columnar, 
    Graph), BASE consistency (Basically Available, Soft state, Eventual 
    consistency), and high horizontal scalability.
*   **Use Cases:** Large-scale web apps, real-time analytics, and 
    unstructured data. Examples include Amazon DynamoDB, MongoDB, and 
    Azure Cosmos DB.
*   **Scaling:** Horizontal (sharding data across multiple servers), 
    allowing for massive throughput and storage.

**Polyglot Persistence:** The practice of using different database 
technologies for different parts of an application to leverage the 
strengths of each model. Architects must evaluate the CAP theorem 
(Consistency, Availability, Partition Tolerance) when selecting a database 
to understand the inherent trade-offs.
"""

version: str = "0.0.1"
