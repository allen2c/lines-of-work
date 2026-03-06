title: str = "Orchestrierung mit Apache Airflow"

content: str = """
Apache Airflow ist eine weit verbreitete Plattform zur Orchestrierung von
Datenpipelines. DAGs (Directed Acyclic Graphs) definieren Tasks und ihre
Abhängigkeiten; der Scheduler führt sie nach Zeitplan oder Trigger aus.

**DAG-Struktur:** Jeder DAG enthält Tasks (Operators). Abhängigkeiten
werden mit set_downstream/set_upstream oder dem >>-Operator definiert.
Zyklische Abhängigkeiten sind nicht erlaubt.

**Operatoren:** PythonOperator für beliebigen Code, BashOperator für
Shell-Befehle, SQL-Befehle über spezifische DB-Operatoren. Custom
Operators kapseln wiederverwendbare Logik.

**Retries und Alerting:** Tasks können bei Fehlern automatisch wiederholt
werden. Nach Ausschöpfung der Retries wird der Task als fehlgeschlagen
markiert; Integration mit Slack/PagerDuty kann Alerts auslösen.

**Best Practices:** DAGs idempotent gestalten, keine schweren Abhängigkeiten
in DAG-Definitionen, sinnvolle Retry-Delays, Ressourcenlimits beachten.
"""

version: str = "0.0.1"
