title = "Schnittdaten und Berechnung"

content = """
- Definitionen: vc Schnittgeschwindigkeit [m/min], f Vorschub [mm/U oder mm/Zahn], ap Schnitttiefe [mm], ae Zustellung [mm].
- Richtwerte vc: 1.0037 S235JR 80 m/min, 1.0577 S355JR 70 m/min, 1.7225 42CrMo4 60–80 m/min (vergütet 50 m/min), 3.3547 AlMg4,5Mn 250–300 m/min, 1.4301 X5CrNi18-10 50–70 m/min, Ti Gr.5 25–35 m/min, POM-C 200–400 m/min, PEEK 100–150 m/min.
- Vorschübe: Fräsen fz 0,05–0,15 mm (Schruppen 0,15, Schlichten 0,05); Drehen f 0,1–0,3 mm/U.
- Drehzahlformel: n [min⁻¹] = vc × 1.000 / (π × d), d in mm.
- Vorschubgeschwindigkeit: vf [mm/min] = fz × z × n (z = Zähnezahl).
- Schnitttiefe: Schruppen ap bis 2 × D, Schlichten 0,2–0,5 mm; Zustellung ae Schruppen 30–50 % D, Schlichten 5–15 % D.
- Erhöhung vc nur, wenn Oberfläche und Standzeit es zulassen; Steigerung max. 15 % pro Schritt, danach 5 min Beobachtung.
- Trockenlauf und Sichtprüfung vor jedem Schnittdatenwechsel, sonst Kollision möglich.
- Bearbeitung von Titan und Edelstahl: stets ausreichend KSS, scharfe Schneide, vc nicht über Herstellerempfehlung.
"""  # noqa: E501

version = "0.0.1"
