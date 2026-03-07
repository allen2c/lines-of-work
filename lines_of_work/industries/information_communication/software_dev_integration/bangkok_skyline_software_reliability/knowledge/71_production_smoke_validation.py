"""
Knowledge item 71: production smoke validation. Verifies core flows work immediately
after deployment to detect regressions before they impact users.
"""

title = "production smoke validation"

content = """
Productie-smokevalidatie controleert direct na een deployment of de kritieke
gebruikersflows en systeemintegraties correct functioneren. Zonder deze validatie
kunnen regressies onopgemerkt blijven totdat gebruikers of monitoring ze signaleren,
waardoor de time-to-detect en impact toenemen.

**Context:** In gedistribueerde API-omgevingen met meerdere services, databases en
externe afhankelijkheden is een geslaagde deploy niet hetzelfde als een correct
werkend systeem. Schema-wijzigingen, configuratiefouten of netwerkproblemen kunnen
pas na de deploy zichtbaar worden. Smoke-tests moeten de belangrijkste happy paths
en integratiepunten raken binnen een korte, voorspelbare tijd.

**Kernprocedures:**
1) Definieer een vaste set smoke-tests die de kritieke flows dekken: authenticatie,
   kern-API-endpoints, database-connectiviteit, en afhankelijkheden van derden.
2) Voer smoke-tests automatisch uit direct na elke productie-deployment, binnen
   dezelfde pipeline of als eerste stap van post-deploy verificatie.
3) Stel een time-out in (bijv. 5–10 minuten); als smoke-tests niet binnen die tijd
   slagen, beschouw de deploy als verdacht en start escalatie of rollback-overweging.
4) Integreer smoke-resultaten met monitoring en alerting; mislukte smoke-tests
   moeten de on-call team waarschuwen en zichtbaar zijn op dashboards.
5) Onderhoud de smoke-suite samen met de architectuur; nieuwe kritieke flows
   moeten worden toegevoegd, verouderde verwijderd.

**Acceptatiecriteria:** Smoke-validatie is effectief wanneer de suite binnen de
time-out draait, alle tests deterministisch zijn, en mislukkingen eenduidig
gekoppeld kunnen worden aan een recente deploy of configuratiewijziging.

**Veelvoorkomende fouten:** Smoke-tests zijn te uitgebreid en vertragen de feedback;
flaky tests veroorzaken valse alarmen; tests raken verouderde endpoints. Mitigatie:
houd de suite klein en stabiel, isoleer externe afhankelijkheden waar mogelijk,
en review de suite bij elke grote architectuurwijziging.
"""  # noqa: E501

version = "0.0.1"
