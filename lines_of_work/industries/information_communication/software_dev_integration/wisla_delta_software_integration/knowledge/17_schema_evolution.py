title = "Ewolucja schematów"

content = """
Schematy danych zmieniają się w czasie. Ewolucja musi być wstecznie kompatybilna,
aby stare klienty i konsumenty nadal działały.

**Zasady:** Dodawaj nowe pola jako opcjonalne. Nie usuwaj pól bez okresu
deprecation. Nie zmieniaj typu istniejącego pola — dodaj nowe. Używaj domyślnych
wartości dla nowych wymaganych pól w starych wersjach.

**Wersjonowanie API:** URL (v1, v2), nagłówek Accept, parametr query. Wycofuj
stare wersje z wyprzedzeniem (6–12 miesięcy).

**Event schemas:** Avro, Protobuf wspierają backward compatibility. JSON Schema
wymaga ręcznej dyscypliny. Rejestr schematów (Schema Registry) pomaga w
śledzeniu wersji.
"""  # noqa: E501

version = "0.0.1"
