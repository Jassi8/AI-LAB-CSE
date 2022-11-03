import networkx as nx
import matplotlib.pyplot as plt

class graphVisualization:
  def __init__(self):
    self.visual = []
  def addedge(self,a,b):
    temp=[a,b]
    self.visual.append(temp)
  def visualize(self):
    G=nx.Graph()
    G.add_edges_from(self.visual)
    nx.draw_networkx(G)
    plt.show()
G=graphVisualization()
G.addedge(0,2)
G.addedge(1,2)
G.addedge(1,3)
G.addedge(5,3)
G.addedge(3,4)
G.addedge(1,0)
G.visualize()