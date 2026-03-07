"""Knowledge item: system context boundary."""

title = "Granice kontekstu systemu"

content = """
Zdefiniowanie granic kontekstu systemu pozwala ustalić, co podlega odpowiedzialności zespołu
niezawodności, a co leży poza jego zakresem. Granice obejmują komponenty wewnętrzne, zależności
zewnętrzne, interfejsy oraz dane przepływające przez system.

**Kontekst:** W architekturze rozproszonej system może obejmować wiele usług, baz danych,
kolejek i zewnętrznych API. Nie wszystkie komponenty są równie krytyczne; granice pomagają
skupić wysiłki na obszarach o najwyższym wpływie na dostępność i integralność danych.

**Kluczowe działania:**
1) Narysuj diagram kontekstu systemu z jasnym rozróżnieniem wewnątrz/na zewnątrz.
2) Zidentyfikuj punkty integracji i ich krytyczność dla biznesu.
3) Udokumentuj założenia dotyczące zewnętrznych zależności (SLA, fallback).
4) Określ, które komponenty wymagają testów chaosu i fault injection.
5) Aktualizuj granice przy zmianach architektury.
"""

version = "0.0.1"
