line = list()
elem = list()
tasks = dict()
file = open('cg.txt', 'r')

for line in file:
    elem = (line.split(','))
    for i in range(len(elem)):
        tasks['T' + str(elem[0])] = dict()
        tasks['T' + str(elem[0])]['id'] = elem[0]
        tasks['T' + str(elem[0])]['name'] = elem[1]
        if (elem[2] != "\n"):
            tasks['T' + str(elem[0])]['predecessors'] = elem[2].strip().split(';')
        else:
            tasks['T' + str(elem[0])]['predecessors'] = []
        tasks['T' + str(elem[0])]['successors'] = []
