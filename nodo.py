# Simulazione di un protocollo di routing utilizzando Distance Vector Routing

# Nome: Tommaso Valeriani
# Email: tommaso.valeriani@studio.unibo.it
# Matricola: 0001081795
# Nome: Federico Panzavolta
# Email: federico.panzavolta@studio.unibo.it
# Matricola: 0001077805

# -*- coding: utf-8 -*-
class Nodo:
    # Inizializzazione di un nuovo nodo
    def __init__(self, nome):
        self.nome = nome
        # Lista dei nodi vicini
        self.vicini = [] 
        # Dizionario per mantenere traccia delle distanze e dei percorsi {destinazione: (distanza, nodo_successivo)}
        self.tabella_routing = {}

    def aggiorna_tabella(self, origine, tabella_esterna):
        # Funzione per aggiornare la tabella di routing del nodo considerato, utilizzando un nodo vicino
        # (origine indica il nome del nodo vicino, e tabella_esterna la sua tabella di routing)
        modificato = False
        for destinazione, (distanza, _) in tabella_esterna.items():
            # Condizione necessaria per ignorare il nodo stesso e non riportarlo nelle tabelle di routing finali
            if destinazione == self.nome:
                continue
    
            # Calcolo della nuova distanza tramite il nodo origine
            costo_stimato = self.tabella_routing.get(origine, (float('inf'), None))[0] + distanza
    
            # Aggiornamento nel caso venga trovato un percorso più breve o una nuova destinazione
            if destinazione not in self.tabella_routing or costo_stimato < self.tabella_routing[destinazione][0]:
                self.tabella_routing[destinazione] = (costo_stimato, origine)
                modificato = True
        return modificato

    # Rappresentazione sotto forma di stringa delle informazioni, in modo da renderle leggibili
    def __str__(self):
        return f"Nodo {self.nome}, Tabella di Routing: {self.tabella_routing}"