import matplotlib as mpl
import matplotlib.pyplot as plt
import ReadData as rd
import scipy as scipy
import networkx as nx
import Schedule

edges = list()
for task in rd.tasks:
    for succ in rd.tasks[task]['successors']:
        arrayInDisguise = list()
        arrayInDisguise.append(int(rd.tasks[task]['id']))
        arrayInDisguise.append(succ)
        edges.append(arrayInDisguise)


G = nx.DiGraph()
dist = dict()

for edge in edges:
    G.add_edge('T' + str(edge[0]), 'T' + str(edge[1]))
    dist['T' + str(edge[0])] = dict()
    dist['T' + str(edge[0])]['T' + str(edge[1])] = 0.2

plt.figure(figsize=(6.4, 4.8))
edgy = [edge for edge in G.edges()]

pos = nx.circular_layout(G)

nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color='teal', node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=edgy, arrows=True)

plt.savefig('circular.png')