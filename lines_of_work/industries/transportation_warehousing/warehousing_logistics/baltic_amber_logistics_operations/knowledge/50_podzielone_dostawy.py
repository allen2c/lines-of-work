title = "Zamówienia podzielone i wysyłki wieloczęściowe"

content = """
Zamówienie może być zrealizowane w wielu przesyłkach
(partial shipment) — np. z powodu braku części towaru
lub celowej strategii (prioritet dla najpilniejszych
pozycji). Magazyn musi śledzić status każdej części.

**Procedura:** WMS dzieli zamówienie na wysyłki. Każda
wysyłka ma własny numer tracking, listę pozycji, dokumenty.
Klient informowany o kolejnych częściach.

**Dokumentacja:** Każda przesyłka z pełną fakturą lub
fakturą pro forma z informacją „część X z Y”. CMR
osobne. W systemie — powiązanie wysyłki z zamówieniem
macierzystym.

**Zamknięcie zamówienia:** Gdy wszystkie części wysłane
— zamówienie w statusie completed. Częściowe płatności
— koordynacja z działem księgowym.
"""  # noqa: E501

version = "0.0.1"
