"""Feature branch release strategy."""

title = "Feature Branch Release Strategy"

content = """
Feature branches moeten op een voorspelbare manier in releases landen. Kies een model:
trunk-based met short-lived branches, of release branches met cherry-picks.

**Trunk-based:** Alle wijzigingen mergen naar main. Releases worden getagd van main. Sneller
maar vereist strikte quality gates op main. Feature flags voor incomplete features.

**Release branches:** Release branch splitst van main op freeze moment. Hotfixes gaan naar
release branch en worden teruggeport naar main. Meer controle, meer merge overhead.

**Consistentie:** Welk model ook: documenteer het, train het team, en handhaaf discipline.
Mixed modellen leiden tot verwarring en merge conflicts.
"""

version = "0.0.1"
