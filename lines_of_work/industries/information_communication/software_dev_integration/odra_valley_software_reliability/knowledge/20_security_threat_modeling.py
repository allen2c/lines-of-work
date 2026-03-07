"""Knowledge item: security threat modeling."""

title = "Modelowanie zagrożeń bezpieczeństwa"

content = """
Modelowanie zagrożeń (threat modeling) identyfikuje potencjalne wektory ataku i słabe
punkty w architekturze. Odra Valley stosuje podejście STRIDE (Spoofing, Tampering,
Repudiation, Information disclosure, Denial of service, Elevation of privilege) lub
równoważne frameworki. Wyniki wpływają na priorytety testów bezpieczeństwa.

**Kontekst:** Bezpieczeństwo jest aspektem niezawodności; luka bezpieczeństwa może
doprowadzić do utraty danych lub niedostępności usługi. Wczesna identyfikacja zagrożeń
jest tańsza niż naprawa po incydencie.

**Kluczowe działania:**
1) Przeprowadź threat modeling dla nowych funkcji i zmian architektury.
2) Udokumentuj zagrożenia, ryzyko i środki zaradcze.
3) Powiąż zagrożenia z testami (np. OWASP ZAP, SAST).
4) Aktualizuj model przy znaczących zmianach.
"""

version = "0.0.1"
