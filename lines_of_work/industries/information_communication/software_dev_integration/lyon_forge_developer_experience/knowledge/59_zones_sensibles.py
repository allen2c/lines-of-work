"""Sensitive areas knowledge for Lyon Forge developer experience."""

title = "Zones sensibles et revue renforcée"

content = """
Certaines zones du code et des configurations exigent une attention particulière. Lyon Forge
identifie ces zones et applique des processus de review renforcés.

**Zones concernées:** Authentification, autorisation, gestion des secrets, accès aux données
personnelles, transactions financières, intégrations externes critiques. Les modifications
du schéma de base de données et des contrats d'API publiques entrent aussi dans cette catégorie.

**Processus:** Revue par au moins deux personnes, vérification manuelle des cas limites,
tests de sécurité ciblés. Les changements doivent être tracés et documentés. En cas de doute,
escalade vers l'équipe sécurité ou l'architecte.

**Formation:** Les développeurs doivent connaître les risques (injection, XSS, exposition
de données) et les patterns sécurisés. La documentation des zones sensibles est maintenue
à jour. Les incidents passés servent de base pour les checklists de review.
"""

version = "0.0.1"
