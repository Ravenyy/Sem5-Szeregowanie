import matplotlib as mpl
import matplotlib.pyplot as plt
import ReadData as rd
import itertools
import CPM as cpm
import scipy as scipy
import networkx as nx

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
    dist['T' + str(edge[0])]['T' + str(edge[1])] = 0.48



plt.figure(figsize =(6.4, 4.8))

CP = list()
red_edges = list()
for task in rd.tasks:
    if (rd.tasks[task]['float'] == 0):
        CP.append(task)

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

for i in pairwise(CP):
    red_edges.append(i)


edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]

black_edges = [edge for edge in G.edges() if edge not in red_edges]

#pos = nx.kamada_kawai_layout(G, dist)
pos = nx.kamada_kawai_layout(G)

nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color = 'teal', node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
plt.show()
