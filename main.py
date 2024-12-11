# Simulazione di un protocollo di routing utilizzando Distance Vector Routing

# Nome: Tommaso Valeriani
# Email: tommaso.valeriani@studio.unibo.it
# Matricola: 0001081795
# Nome: Federico Panzavolta
# Email: federico.panzavolta@studio.unibo.it
# Matricola: 0001077805

# -*- coding: utf-8 -*-
from rete import Rete

# Creazione della rete
rete = Rete()
rete.aggiungi_nodo("A")
rete.aggiungi_nodo("B")
rete.aggiungi_nodo("C")
rete.aggiungi_nodo("D")

# Creazione dei collegamenti tra nodi
rete.collega_nodi("A", "B", 1)
rete.collega_nodi("B", "C", 2)
rete.collega_nodi("C", "D", 1)
rete.collega_nodi("A", "D", 4)

# Tabelle di routing iniziali
print("Tabelle di routing iniziali:")
rete.stampa_tabelle()

# Propagazione dei messaggi di routing
rete.propaga_messaggi()

# Tabelle di routing finali
print("\nTabelle di routing finali:")
rete.stampa_tabelle()