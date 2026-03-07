"""Criteria for deciding when to rollback a release."""

title = "Rollback Decision Criteria"

content = """
Definieer vooraf wanneer een rollback wordt uitgevoerd. Criteria omvatten: significante
stijging van error rate, degradatie van latency beyond SLO, data corruption of
verlies, security incident, of onvermogen om kritieke functionaliteit te leveren.
Stel drempelwaarden vast (bijv. error rate > 1% gedurende 5 minuten). Het besluit
moet snel genomen worden; twijfel leidt tot langere impact. Documenteer wie
geautoriseerd is om rollback te initiëren.
"""

version = "0.0.1"
