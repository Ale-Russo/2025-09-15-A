import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._DriversMap = {}

    def getAllYears(self):
        return DAO.getAllYears()

    def creaGrafo(self, y1, y2):
        grafo = self._grafo
        grafo.clear()
        nodi = DAO.getAllNodes(y1, y2)
        for n in nodi:
            self._DriversMap[n.driverId] = n

        archi = DAO.getAllEdges(y1, y2, self._DriversMap)
        grafo.add_nodes_from(nodi)
        for a in archi:
            grafo.add_edge(a.d1, a.d2, weight=a.peso)

    def dettagliGrafo(self):
        grafo = self._grafo
        nNodi = len(grafo.nodes())
        nArchi = len(grafo.edges())
        archi = grafo.edges(data=True)
        archiOrdinati = sorted(archi, key=lambda x: x[2]['weight'], reverse=True)
        bestTre = archiOrdinati[:3]
        compConn = list(nx.connected_components(grafo))
        nComp = len(compConn)
        maxComp = max(compConn)
        return nNodi, nArchi, bestTre, nComp, maxComp




