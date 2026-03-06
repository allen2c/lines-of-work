title = "Access Control und RBAC"

content = """
Role-Based Access Control (RBAC) vergibt Berechtigungen über Rollen statt
individuell. Prinzip der minimalen Rechte: Nutzer erhalten nur die
Berechtigungen, die für ihre Aufgabe nötig sind. Typische Rollen:
Data-Engineer (Lesen/Schreiben in Dev, Lesen in Prod), Analyst (Lesen in
bestimmten Schemas), Admin (volle Rechte). Rollen in Snowflake, Databricks
und Kafka getrennt konfigurieren. Änderungen an Berechtigungen protokollieren.
Bei Ausscheiden von Mitarbeitern Zugriff umgehend entziehen. Regelmäßige
Recertification der Zugriffsrechte.
"""

version = "0.0.1"
