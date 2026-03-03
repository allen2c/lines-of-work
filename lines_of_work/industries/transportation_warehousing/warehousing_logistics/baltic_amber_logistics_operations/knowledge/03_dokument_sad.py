title = "Dokument SAD i powiązania z WMS"

content = """
SAD (Single Administrative Document) to wspólny dokument celny UE używany
przy przywozie, wywozie lub tranzycie towarów. Każda pozycja w SAD
odnosi się do konkretnej partii towaru i musi być powiązana z rekordem
w systemie magazynowym.

**Mapowanie pozycji:** Numer pozycji SAD, numer HS, waga netto i brutto,
ilość sztuk — wszystkie pola muszą zgadzać się z danymi w WMS. Rozbieżność
uniemożliwia prawidłową odprawę i generuje opóźnienia na granicy.

**Cykl życia:** Po otrzymaniu przesyłki sprawdzamy SAD względem faktury
i fizycznej zawartości. Wpis w WMS tworzy powiązanie SAD–SKU–lokalizacja.
Przy wysyłce eksportowej generujemy nowy SAD lub referencję do istniejącego.

**Archiwizacja:** Skan każdego SAD przechowujemy w systemie. Oryginały
przechowywane w archiwum minimum 5 lat zgodnie z przepisami celnych.
"""  # noqa: E501

version = "0.0.1"
