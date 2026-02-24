title: str = "Cloud Service Models: IaaS, PaaS, SaaS, and FaaS"

content: str = """
Cloud service models describe the division of responsibility between the 
cloud provider and the customer. Understanding these models is critical for 
defining the operational scope of an architectural design.

**Infrastructure as a Service (IaaS):** The provider offers fundamental 
compute, storage, and networking resources. The customer is responsible for 
managing the operating system, middleware, and applications. IaaS provides the 
maximum flexibility and control, similar to traditional on-premises data 
centers but with cloud scalability.

**Platform as a Service (PaaS):** The provider manages the underlying 
infrastructure and the operating system, providing a platform for developers 
to build, deploy, and manage applications. This model reduces operational 
overhead, allowing teams to focus on code rather than server maintenance. 
Examples include Azure App Service and AWS Elastic Beanstalk.

**Software as a Service (SaaS):** The provider delivers a complete software 
application over the internet. The customer has no responsibility for the 
underlying infrastructure or application maintenance. Examples include 
Microsoft 365 and Salesforce.

**Function as a Service (FaaS) / Serverless:** A subset of PaaS where the 
provider manages the execution of individual functions in response to events. 
Customers only pay for the actual execution time. This model enables extreme 
scalability and "zero-scale" cost efficiency, but introduces challenges in 
state management and cold-start latency.
"""

version: str = "0.0.1"
