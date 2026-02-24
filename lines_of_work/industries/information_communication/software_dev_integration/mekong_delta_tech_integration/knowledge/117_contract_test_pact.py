title = "Contract Test với Pact"

content = """
Pact: consumer-driven contract testing. Consumer define expectation. Provider
verify. Mekong Delta Tech dùng Pact cho integration. Catch breaking change.

**Consumer Test:** Consumer test với Pact mock. Define request, expected response.
Generate contract. Publish to broker. Or file. Version. CI. Fail if expectation
change without intent.

**Provider Test:** Provider verify against contract. Pact mock request. Verify
actual response match. CI. Fail if provider break contract. Before deploy.
Fix or coordinate. Consumer update? New contract. Provider verify new.

**Broker:** Central contract store. Pact Broker. Version. Tag. Can I deploy?
Contract compatible? Integration. CI/CD. Matrix. Document. Best practice.
"""  # noqa: E501

version = "0.0.1"
