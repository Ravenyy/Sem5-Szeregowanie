line = list()
elem = list()
tasks = dict()
file = open('br.txt', 'r')

for line in file:
    elem = (line.split(','))
    for i in range(len(elem)):
        tasks['T' + str(elem[0])] = dict()
        tasks['T' + str(elem[0])]['id'] = elem[0]
        tasks['T' + str(elem[0])]['name'] = elem[1]
        tasks['T' + str(elem[0])]['duration'] = elem[2]
        if (elem[3] != "\n"):
            tasks['T' + str(elem[0])]['predecessors'] = elem[3].strip().split(';')
        else:
            tasks['T' + str(elem[0])]['predecessors'] = []
        tasks['T' + str(elem[0])]['successors'] = []
        tasks['T' + str(elem[0])]['d'] = []
        tasks['T' + str(elem[0])]['L'] = []
        tasks['T' + str(elem[0])]['start'] = []
        tasks['T' + str(elem[0])]['end'] = []


actualSuccs = list()
actualSuccs.append("0")
for i in tasks:
    actualSuccs.append(tasks[i]['predecessors'])

for succ in range(len(actualSuccs)):
    for node in actualSuccs[succ]:
        if (int(node) > 0):
            tasks['T' + node]['successors'].append(succ)

tempKeys = list()
for element in tasks.keys():
    tempKeys.append(element)

reversedKeys = list()
while len(tempKeys) > 0:
    reversedKeys.append(tempKeys.pop())

noSuccs = list()
for task in tasks:
    if not tasks[task]['successors']:
        noSuccs.append(task)