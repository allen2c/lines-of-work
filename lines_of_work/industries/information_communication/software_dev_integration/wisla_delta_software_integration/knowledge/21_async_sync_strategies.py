title = "Strategie synchroniczne i asynchroniczne"

content = """
Integracje mogą działać synchronicznie (żądanie–odpowiedź) lub asynchronicznie (kolejka, zdarzenia).
Wybór zależy od wymagań dotyczących opóźnienia, niezawodności i przepływności.

**Synchroniczne:** Klient czeka na odpowiedź. Odpowiednie dla operacji szybkich, gdy natychmiastowa
reakcja jest kluczowa. Ryzyko: timeouty, blokowanie przy awarii zdalnego systemu.

**Asynchroniczne:** Wiadomość trafia do kolejki lub brokera; przetwarzanie odbywa się później.
Lepsze dla długotrwałych zadań, dużych wolumenów i scenariuszy odpornych na opóźnienia.
"""  # noqa: E501

version = "0.0.1"
