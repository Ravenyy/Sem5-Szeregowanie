from airium import Airium
import ReadData as rd

edgesList = list()
for task in rd.tasks:
    for succ in rd.tasks[task]['successors']:
        arrayInDisguise = list()
        arrayInDisguise.append(int(rd.tasks[task]['id']))
        arrayInDisguise.append(succ)
        edgesList.append(arrayInDisguise)

doc = Airium()
nodes = ''
edges = ''

for i in rd.tasks:
    nodes += "\t\t{id: " + str(rd.tasks[i]['id']) + ", label: '" + rd.tasks[i]['name'] + "," + rd.tasks[i]['duration'] + "'},\n"

for i in edgesList:
    edges += "\t\t{from: " + str(i[0]) + ", to: " + str(i[1]) + ", arrows: 'to'},\n"

with doc.html():
    with doc.head():
        doc.script(type='text/javascript', src='https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js')
        doc.link(href='https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css', rel='stylesheet', type='text/css')
        with doc.style(type='text/css'):
            doc("\t#mynetwork {\n\t\twidth: 1400px;\n\t\theight: 1200px;\n\t\tborder: 1px solid lightgray;\n\t}")


    with doc.body():
        doc.div(id='mynetwork')
        with doc.script(type='text/javascript'):
            doc("\n\tvar nodes = new vis.DataSet([\n" + nodes + "\t]);")
            doc("\n\tvar edges = new vis.DataSet([\n" + edges + "\t]);")
            doc("\n\tvar container = document.getElementById('mynetwork');")
            doc("\n\tvar data = {\n\t\t nodes: nodes, \n\t\t edges: edges,\n\t};")
            doc("\n\tvar options = {};")
            doc("\n\tvar network = new vis.Network(container, data, options);")

f = open("Graf.html", "w")
f.write(str(doc))
f.close()