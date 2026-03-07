"""Deployment scheduling best practices."""

title = "Deployment Scheduling Best Practices"

content = """
Plan deployments op momenten met lage impact. Vermijd piekuren, belangrijke handelsdagen, of
periodes direct na grote wijzigingen. Houd rekening met tijdzones van gebruikers en support.

**Vaste vensters:** Wekelijkse of bi-weekly deployment windows creëren voorspelbaarheid.
Communiceer vensters ruim van tevoren. Onderhoudsvensters voor breaking changes.

**Buffer:** Plan buffer tussen deployment en volgende kritieke activiteit. Bij problemen
moet er tijd zijn voor rollback of fix zonder druk.

**Coördinatie:** Bij gedeelde infrastructuur: coördineer met andere teams. Release freezes
tijdens kritieke periodes (bijv. jaarwisseling) moeten gedocumenteerd zijn.
"""

version = "0.0.1"
