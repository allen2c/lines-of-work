title = "Planowanie fal kompletacji w eksporcie"

content = """
Fale kompletacji grupują zamówienia według przewoźnika, trasy,
priorytetu lub typu towaru. Optymalizują ścieżki pracowników
i minimalizują czas realizacji zbiorczych wysyłek.

**Kryteria podziału:** Przewoźnik (np. cała fala DHL do Litwy),
godzina odbioru, ekspres vs standard. System WMS przypisuje
zamówienia do fal na podstawie reguł konfiguracyjnych.

**Częstotliwość fal:** W szczycie — co 2–4 godziny. W okresie
standardowym — 1–2 fale dziennie na przewoźnika. Zamówienia
ekspresowe — fala natychmiastowa.

**Koordynacja:** Kierownik zmiany ogłasza zamknięcie fali.
Wszystkie zamówienia z zamkniętej fali muszą być skompletowane,
spakowane i zweryfikowane przed manifestacją.
"""  # noqa: E501

version = "0.0.1"
