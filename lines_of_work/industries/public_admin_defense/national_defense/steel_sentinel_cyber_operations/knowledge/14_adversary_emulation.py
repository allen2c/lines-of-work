title = "Adversary Emulation and Red Team Operations"

content = """
Adversary emulation — systematically replicating known adversary tactics, techniques,
and procedures against the unit's own defenses — is one of the most effective methods
for validating detection and response capabilities before a real adversary exploits
gaps. The unit participates in both internal and externally conducted adversary
emulation events.

**Internal Purple Team Exercises:** Analysts from the cyber operations team work
alongside authorized red team operators who simulate adversary TTPs drawn from
the MITRE ATT&CK framework. Blue team defenders observe detections in real time,
identify misses, and tune detection rules. Results are documented in a structured
exercise report with detection coverage mapped to ATT&CK technique IDs.

**External Red Team Events:** Higher headquarters may task an independent red team
to conduct an unannounced adversary simulation against the unit's defenses. The unit
cooperates fully, providing post-event access to logs and telemetry to enable the
red team to complete their final report. No defensive action taken during the exercise
should be withheld from the after-action review.

**Scope and Safety Rules:** Every exercise has a written scope document (sometimes called
a get-well letter or deconfliction document) specifying which systems are in scope, what
techniques are authorized, and what conditions would trigger an exercise pause. The unit
commander and the red team lead must both sign before the exercise begins.

**Incorporating Findings:** Detection gaps identified in exercises are tracked as formal
findings with assigned owners and remediation dates. The unit measures exercise-over-
exercise improvement in detection coverage as a key performance indicator of the
effectiveness of the cyber defense program.
"""

version = "0.0.1"
