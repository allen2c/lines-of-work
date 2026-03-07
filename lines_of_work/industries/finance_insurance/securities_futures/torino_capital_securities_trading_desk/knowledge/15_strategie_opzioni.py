"""
Knowledge item 15: options strategies. Common option structures used in trading
and hedging.
"""

title = "strategie opzioni"

content = """
Le strategie su opzioni combinano call e put con diverse scadenze e strike per
creare payoff specifici. La desk deve comprendere le strutture comuni per
esecuzione, hedging e consulenza ai clienti.

**Call e Put plain vanilla:** Una call dà il diritto di acquistare il sottostante
allo strike; una put il diritto di vendere. Il premio dipende da prezzo spot,
strike, scadenza, volatilità e tassi.

**Spread:** Gli spread verticali combinano call o put a strike diversi (bull/bear
spread). Gli spread a farfalla e condor aggiungono gambe per limitare rischio
e costo. Gli spread orizzontali (calendar) sfruttano il time decay differenziale.

**Straddle e Strangle:** Lo straddle acquista call e put allo stesso strike,
profittando di grandi movimenti in entrambe le direzioni. Lo strangle usa strike
out-of-the-money per ridurre il costo a scapito di un break-even più ampio.

**Covered call e protective put:** Il covered call vende call su posizioni
esistenti per generare premio. Il protective put acquista put per proteggere
posizioni long da ribassi.

**Delta hedging:** I market maker e i desk di derivati neutralizzano il delta
con operazioni sul sottostante, adeguando dinamicamente al variare del prezzo.

**Greeks:** Delta, gamma, theta, vega e rho misurano la sensibilità del premio.
La gestione del rischio richiede il monitoraggio continuo dei Greeks.
"""  # noqa: E501

version = "0.0.1"
