title: str = "Cloud Compliance and Data Sovereignty"

content: str = """
Compliance in the cloud ensures that an organization's infrastructure and 
processes adhere to legal, regulatory, and industry standards. Data 
Sovereignty refers to the concept that digital data is subject to the laws 
of the country in which it is located.

**Key Regulatory Frameworks:**
1. **GDPR (General Data Protection Regulation):** Governs data protection 
   and privacy for individuals within the European Union. It includes 
   strict requirements for data residency and the "right to be forgotten."
2. **HIPAA (Health Insurance Portability and Accountability Act):** Sets 
   the standard for protecting sensitive patient data in the United States.
3. **PCI DSS (Payment Card Industry Data Security Standard):** A set of 
   security standards designed to ensure that all companies that accept, 
   process, store, or transmit credit card information maintain a secure 
   environment.

**Architectural Implications:**
*   **Region Selection:** Architects must choose cloud regions that align 
    with the data residency requirements of their clients.
*   **Data Encryption:** Implementing robust encryption (at rest and in 
    transit) using customer-managed keys (CMK) to maintain control over 
    data access.
*   **Audit Logging:** Maintaining immutable logs of all data access and 
    configuration changes to demonstrate compliance during audits.

Failure to address compliance and sovereignty can lead to significant 
legal penalties and loss of customer trust.
"""

version: str = "0.0.1"
