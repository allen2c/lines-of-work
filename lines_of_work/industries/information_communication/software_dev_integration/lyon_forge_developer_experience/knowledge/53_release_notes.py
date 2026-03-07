"""Release notes knowledge for Lyon Forge developer experience."""

title = "Notes de release et changelog"

content = """
Les notes de release informent les utilisateurs et les équipes des changements. À Lyon Forge,
chaque release majeure ou mineure est accompagnée de notes structurées et exploitables.

**Format:** Utilisez Keep a Changelog ou un format similaire : Added, Changed, Deprecated, Removed,
Fixed, Security. Chaque entrée doit être une phrase complète, orientée utilisateur. Évitez le
jargon technique excessif pour les releases externes.

**Processus:** Les développeurs ajoutent des entrées au changelog dans leur PR. Un script ou
un outil peut agréger les entrées par version. Les notes finales sont révisées avant publication
pour cohérence et clarté.

**Public:** Adaptez le ton et le niveau de détail selon l'audience (interne vs client, technique
vs fonctionnel). Les breaking changes doivent être mis en évidence avec des instructions de
migration claires.
"""

version = "0.0.1"
