from model.model import Model

myModel = Model()
myModel.creaGrafo(2007,2008)
print(f"Il grafo ha {len(myModel._grafo.nodes)} nodi e {len(myModel._grafo.edges)} archi.")
