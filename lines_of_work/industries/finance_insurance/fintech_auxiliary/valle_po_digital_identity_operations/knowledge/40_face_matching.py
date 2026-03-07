"""Confronto facciale documento-foto live."""

title = "Confronto Facciale Documento-Foto Live"

content = """
Il face matching confronta la foto sul documento con un selfie o frame
video live. Deve superare una soglia di similarità configurata. Fattori che
influenzano: illuminazione, angolazione, occhiali, invecchiamento. Per
liveness, si richiede che il selfie sia acquisito in tempo reale (non
foto pre-scattata). Fallimenti possono essere dovuti a qualità immagine
o variazioni fisionomiche; in tal caso si propone retry o video-ID.
"""  # noqa: E501

version = "0.0.1"
