title = "Reset password e gestione account"

content = """
- Per reset password: verifica l'identità tramite domanda di sicurezza o chiamata al numero interno. Non accettare richieste via email non crittografata.
- Utilizza lo strumento di self-service (Azure SSPR) se disponibile; altrimenti reimposta manualmente in AD e comunica la nuova password temporanea.
- Per sblocco account: controlla se l'account è bloccato per troppi tentativi errati. Sblocca e consiglia all'utente di cambiare password.
- Per MFA: se l'utente ha perso il telefono, reimposta i metodi di autenticazione dopo verifica con il manager.
"""  # noqa: E501

version = "0.0.1"
