title = "Gestione materiali e logistica di linea"

content = """
- I materiali arrivano al magazzino di linea tramite carrelli o AGV. Ogni bobina di nastro ha un codice lotto e una quantità residua.
- Utilizzare il sistema MES per tracciare il consumo: scannerizzare il codice a barre del feeder quando montato e quando rimosso.
- Per evitare fermi, mantenere un buffer di 2 ore di componenti per ogni feeder. Se un componente è in esaurimento, generare un alert.
- Smaltire i nastri vuoti e i rifiuti di pasta saldante secondo le normative ambientali (RAEE, rifiuti pericolosi).
"""

version = "0.0.1"
