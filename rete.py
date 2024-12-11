# Simulazione di un protocollo di routing utilizzando Distance Vector Routing

# Nome: Tommaso Valeriani
# Email: tommaso.valeriani@studio.unibo.it
# Matricola: 0001081795
# Nome: Federico Panzavolta
# Email: federico.panzavolta@studio.unibo.it
# Matricola: 0001077805

# -*- coding: utf-8 -*-
from nodo import Nodo

class Rete:
    def __init__(self):
        self.nodi = {}
        self.connessioni = {}

    def aggiungi_nodo(self, nome):
        self.nodi[nome] = Nodo(nome)

    def collega_nodi(self, nodo1, nodo2, costo):
        # Aggiornamento delle connessioni
        self.connessioni.setdefault(nodo1, {})[nodo2] = costo
        self.connessioni.setdefault(nodo2, {})[nodo1] = costo
        
        # Aggiunta dei nodi alla lista dei vicini
        self.nodi[nodo1].vicini.append(nodo2)
        self.nodi[nodo2].vicini.append(nodo1)
        
        # Aggiornamento delle tabelle di routing iniziali
        self.nodi[nodo1].tabella_routing[nodo2] = (costo, nodo2)
        self.nodi[nodo2].tabella_routing[nodo1] = (costo, nodo1)

    def propaga_messaggi(self):
        # Funzione per propagare i messaggi tra i nodi della rete
        # e aggiornare le tabelle di routing, questo viene ripetuto finchè
        # non ci saranno più modifiche alle tabelle di routing
        modificato = True
        # Eseguo un ciclo finchè il flag "modificato" non viene aggiornato
        while modificato:
            modificato = False
            # Eseguo un ciclo per ogni nodo della rete
            for nodo_nome, nodo in self.nodi.items():
                # Eseguo un ciclo sui vicini di ogni nodo
                for vicino, costo in self.connessioni.get(nodo_nome, {}).items():
                    vicino_nodo = self.nodi[vicino]
                    # verifica se la tabella di routing del nodo sia da aggiornare
                    if nodo.aggiorna_tabella(vicino, vicino_nodo.tabella_routing):
                        # In caso positivo il flag viene inpostato a TRUE per
                        # permettere al ciclo di continuare
                        modificato = True
                        
    # Stampo le tabelle di routing
    def stampa_tabelle(self):
        for nodo in self.nodi.values():
            print(nodo)