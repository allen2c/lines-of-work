title: str = "Infrastructure as Code (IaC) and Automation"

content: str = """
Infrastructure as Code (IaC) is the practice of managing and provisioning 
computing infrastructure through machine-readable definition files, rather 
than physical hardware configuration or interactive configuration tools.

**Key Benefits:**
1. **Consistency:** Eliminates "configuration drift" by ensuring the 
   environment is always in the state defined by the code.
2. **Speed and Agility:** Allows for rapid deployment of entire 
   environments through automated pipelines.
3. **Version Control:** Infrastructure changes can be tracked, reviewed, 
   and rolled back using standard Git workflows.

**IaC Approaches:**
*   **Declarative (Functional):** You define the "what"—the desired end 
    state of the infrastructure. The tool (e.g., Terraform, CloudFormation) 
    figures out how to achieve that state.
*   **Imperative (Procedural):** You define the "how"—the specific steps or 
    commands required to provision the resources (e.g., AWS CLI scripts, 
    Ansible).

**Immutable Infrastructure:** A pattern where servers are never modified 
after deployment. If a change is needed, a new server is built from a 
common image with the changes applied, and the old one is destroyed. This 
reduces unpredictable behavior and simplifies troubleshooting.
"""

version: str = "0.0.1"
