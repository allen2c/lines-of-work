"""
Knowledge item 07: portfolio risk metrics. Core risk measures for trading positions.
"""

title = "metriche di rischio di portafoglio"

content = """
Le metriche di rischio di portafoglio quantificano l'esposizione del desk di trading a
variazioni di mercato, liquidità e controparte. Sono essenziali per il monitoraggio in
tempo reale e il rispetto dei limiti di rischio.

**Value at Risk (VaR)** stima la perdita massima attesa in un orizzonte temporale dato
con un livello di confidenza (es. 95% o 99%). Il metodo parametrico assume distribuzioni
normali; la simulazione storica usa dati storici; Monte Carlo genera scenari casuali.
Ogni approccio ha compromessi tra precisione, velocità e ipotesi.

**Expected Shortfall (ES)** misura la perdita media oltre il VaR, catturando la coda
della distribuzione. È più conservativo del VaR e preferito da regolatori (Basel III).

**Greci (opzioni)** quantificano la sensibilità: Delta (prezzo sottostante), Gamma
(curvatura), Vega (volatilità), Theta (tempo), Rho (tassi). Per portafogli complessi
i greci aggregati guidano le decisioni di copertura.

**Stress test** applica scenari estremi (crollo mercato, crisi liquidità, default
controparte) per valutare perdite potenziali in condizioni anomale.

**Concentration risk** misura l'esposizione a singoli emittenti, settori o controparti.
Limiti di concentrazione prevengono perdite eccessive da eventi idiosincratici.

**Liquidity risk** valuta la capacità di chiudere posizioni senza impatto eccessivo
sul prezzo. Bid-ask spread, depth e volume informano le metriche di liquidità.
"""  # noqa: E501

version = "0.0.1"
