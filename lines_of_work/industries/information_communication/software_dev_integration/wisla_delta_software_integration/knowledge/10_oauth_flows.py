title = "Przepływy OAuth"

content = """
OAuth 2.0 to standard autoryzacji dla API. Integracje często wymagają dostępu do
zasobów w imieniu użytkownika lub aplikacji — OAuth definiuje, jak uzyskać i używać
tokenów dostępu.

**Client Credentials:** Dla integracji machine-to-machine (serwis do serwisu). Klient
wymienia client_id i client_secret na token. Brak kontekstu użytkownika.

**Authorization Code:** Dla aplikacji z użytkownikiem. Użytkownik jest przekierowywany
do dostawcy, loguje się, dostawca zwraca kod do callback URL. Aplikacja wymienia kod
na token. Bezpieczniejsze — secret nie jest eksponowany w przeglądarce.

**Refresh token:** Tokeny dostępu wygasają (np. po godzinie). Refresh token pozwala
uzyskać nowy access token bez ponownej autoryzacji użytkownika. Przechowuj refresh
tokeny bezpiecznie i odnawiaj access token przed wygaśnięciem.

**PKCE:** Dla aplikacji publicznych (SPA, mobile) — Proof Key for Code Exchange
zabezpiecza przed przechwyceniem kodu autoryzacji.
"""  # noqa: E501

version = "0.0.1"
