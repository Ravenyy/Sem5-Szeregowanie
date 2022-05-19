import plotly.graph_objects as go
import plotly.offline as py
import ReadData as rd
import CPM
import networkx as nx

edges = list()

for task in rd.tasks:
    for succ in rd.tasks[task]['successors']:
        arrayInDisguise = list()
        arrayInDisguise.append(int(rd.tasks[task]['id']))
        arrayInDisguise.append(succ)
        edges.append(arrayInDisguise)

G = nx.Graph()


for task in rd.tasks:
    G.add_node(task, size = 5)

for edge in edges:
    G.add_edge('T' + str(edge[0]), 'T' + str(edge[1]), weight = 3)

pos_ = nx.graphviz_layout(G)

def make_edge(x, y, text, width):
    return  go.Scatter(x = x, y = y, line = dict(width = width, color = 'cornflowerblue'), hoverinfo = 'text',
                       text = ([text]), mode = 'lines')


edge_trace = []

for edge in G.edges():
    point1 = edge[0]
    point2 = edge[1]
    x0, y0 = pos_[point1]
    x1, y1 = pos_[point2]
    text = point1 + '--' + point2 + ': ' + str(G.edges()[edge]['weight'])

    trace = make_edge([x0, x1, None], [y0, y1, None], text, width=0.3)
    edge_trace.append(trace)


node_trace = go.Scatter(x = [], y = [], text = [], textposition = "top center", textfont_size = 10,
                        mode = 'markers+text', hoverinfo = 'none', marker = dict(color = [], size = [],
                        line = None))

for node in G.nodes():
    x, y = pos_[node]
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])
    node_trace['marker']['color'] += tuple(['cornflowerblue'])
    node_trace['marker']['size'] += tuple([5*G.nodes()[node]['size']])
    node_trace['text'] += tuple(['<b>' + node + ', ' + str(rd.tasks[node]['duration']) + '</b>'])

layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)', # transparent background
    plot_bgcolor='rgba(0,0,0,0)', # transparent 2nd background
    xaxis =  {'showgrid': False, 'zeroline': False}, # no gridlines
    yaxis = {'showgrid': False, 'zeroline': False}, # no gridlines
)

fig = go.Figure(layout = layout)

for trace in edge_trace:
    fig.add_trace(trace)

fig.add_trace(node_trace)

fig.update_layout(showlegend = False)

fig.update_xaxes(showticklabels = False)

fig.update_yaxes(showticklabels = False)

fig.show()