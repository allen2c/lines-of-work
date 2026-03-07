"""
Knowledge item 16: futures contracts. Mechanics of futures trading and clearing.
"""

title = "contratti futures"

content = """
I contratti futures sono accordi standardizzati per acquistare o vendere un
attività a un prezzo fissato in una data futura. Sono negoziati su borse
regolamentate e compensati da clearing house centrali.

**Struttura:** Ogni contratto specifica il sottostante, la dimensione, la
scadenza e le modalità di regolamento (fisico o cash). I futures su indici
azionari si regolano in contanti; quelli su materie prime spesso in fisico.

**Margini:** I trader depositano margine iniziale e ricevono margin call quando
il margine di mantenimento scende sotto la soglia. La clearing house garantisce
la performance tramite il sistema dei margini.

**Mark-to-market:** Le posizioni sono valorizzate giornalmente (mark-to-market).
I profitti e le perdite sono accreditati o addebitati quotidianamente sui
conti margine.

**Roll:** All'avvicinarsi della scadenza, i trader rollano le posizioni sul
contratto successivo per evitare la consegna. La curva dei futures (contango,
backwardation) influenza il costo del roll.

**Arbitraggio:** L'arbitraggio cash-and-carry lega i prezzi dei futures ai
prezzi spot tramite costi di finanziamento e di stoccaggio. Le deviazioni
creano opportunità di arbitraggio.

**Microstructure:** I futures su indici e tassi sono tra gli strumenti più
liquidi al mondo. I futures su materie prime hanno liquidità variabile per
scadenza e sottostante.
"""  # noqa: E501

version = "0.0.1"
