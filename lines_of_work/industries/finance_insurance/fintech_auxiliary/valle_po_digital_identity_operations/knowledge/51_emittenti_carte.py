"""Knowledge for card issuer identity verification requirements."""

title = "Emittenti Carte e Requisiti Verifica"

content = """
Gli emittenti di carte (banche, FinTech) devono verificare l'identità dei titolari
prima dell'emissione. Valle Po supporta flussi dedicati per onboarding carte.

**Requisiti:** Carta d'identità o passaporto valido, prova di residenza, e talvolta
verifica del reddito per limiti di credito. Per carte business: documentazione
aziendale e UBO.

**Integrazione:** API specifiche per emittenti, con webhook su stato verifica.
Supporto per pre-approvazione e verifica post-attivazione.

**Conformità:** PSD2 SCA, regole scheme (Visa, Mastercard) su KYC per carte.
"""  # noqa: E501

version = "0.0.1"
