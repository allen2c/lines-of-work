"""
Knowledge item 70: cost of quality tracking. Tracks prevention, appraisal, and failure
costs to optimize reliability investments and justify quality gates.
"""

title = "cost of quality tracking"

content = """
Il tracciamento del costo della qualità (CoQ) consente di quantificare gli investimenti
in affidabilità e di bilanciarli rispetto al costo degli incidenti e delle regressioni.
Senza questa metrica, le decisioni sui quality gate e sulle attività di test restano
basate su intuizioni anziché su dati economici verificabili.

**Contesto:** In servizi API ad alto traffico, il costo della qualità si divide in tre
categorie: costi di prevenzione (design, review, test preventivi), costi di valutazione
(test, monitoraggio, audit), e costi di fallimento (incidenti, rollback, riparazioni,
perdita di fiducia). Un modello CoQ ben definito aiuta a giustificare investimenti
in test e osservabilità e a identificare dove il rapporto costo-beneficio è sbilanciato.

**Procedure principali:**
1) Classificare le attività di reliability in prevenzione, valutazione o fallimento,
   e assegnare stime di costo (tempo, risorse, tool) per ciascuna.
2) Tracciare il costo degli incidenti: tempo di risoluzione, impatto sul business,
   rollback, hotfix e postmortem. Includere il costo opportunità e il danno reputazionale.
3) Calcolare periodicamente il rapporto CoQ (prevenzione + valutazione) vs. costo
   dei fallimenti. Un rapporto troppo basso indica sottoinvestimento in qualità;
   uno troppo alto può indicare inefficienza o over-testing.
4) Collegare i CoQ ai quality gate: ogni gate deve avere una giustificazione economica
   (riduzione attesa del costo di fallimento) documentata e rivista trimestralmente.
5) Comunicare i trend CoQ agli stakeholder per supportare decisioni su budget,
   priorità di test e tolleranza al rischio.

**Criteri di accettazione:** Il tracciamento CoQ è operativo quando almeno tre
categorie sono misurate, i dati sono aggiornati mensilmente, e esiste un report
trimestrale che collega gli investimenti ai risultati (riduzione incidenti, MTTR).

**Errori comuni:** Ignorare i costi indiretti (stress del team, ritardi su altri
progetti); non includere il costo delle regressioni scoperte in produzione; usare
stime invece di dati reali. Mitigazione: integrare CoQ con ticket system e
timesheet, e rivedere le stime con dati storici ogni semestre.
"""  # noqa: E501

version = "0.0.1"
