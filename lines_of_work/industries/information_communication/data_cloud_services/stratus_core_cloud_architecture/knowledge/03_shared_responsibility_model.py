title: str = "The Shared Responsibility Model in Cloud Security"

content: str = """
The Shared Responsibility Model is a fundamental security framework that 
clarifies which security tasks are handled by the cloud provider and which 
are the responsibility of the customer. Misunderstanding this model is a 
leading cause of cloud security breaches.

**Provider Responsibility (Security 'of' the Cloud):** The cloud provider is 
responsible for protecting the infrastructure that runs all of the services 
offered in the cloud. This includes the physical security of data centers, 
the hardware, the virtualization layer, and the global network infrastructure.

**Customer Responsibility (Security 'in' the Cloud):** The customer's 
responsibility is determined by the cloud service model (IaaS, PaaS, or SaaS). 
In IaaS, the customer is responsible for patching the guest OS, configuring 
network firewalls (Security Groups), managing identity and access (IAM), and 
encrypting data at rest and in transit. In SaaS, the responsibility shifts 
primarily to data management and access control.

**Shared Responsibilities:** Some areas, such as Identity and Access 
Management (IAM) and Patch Management, often involve shared duties. For 
instance, the provider ensures the IAM service is available and secure, but 
the customer is responsible for defining the policies and ensuring 
least-privilege access.

Architects must explicitly document the boundary of responsibility for every 
component in a cloud system to ensure no security gaps exist between the 
provider's controls and the customer's configurations.
"""

version: str = "0.0.1"
