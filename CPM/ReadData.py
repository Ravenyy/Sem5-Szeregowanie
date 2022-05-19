line = list()
elem = list()
tasks = dict()
file = open('cpm.txt', 'r')

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
            tasks['T' + str(elem[0])]['predecessors'] = ['-1']
        tasks['T' + str(elem[0])]['ES'] = 0
        tasks['T' + str(elem[0])]['EF'] = 0
        tasks['T' + str(elem[0])]['LS'] = 0
        tasks['T' + str(elem[0])]['LF'] = 0
        tasks['T' + str(elem[0])]['float'] = 0
        tasks['T' + str(elem[0])]['isCritical'] = False
        tasks['T' + str(elem[0])]['successors'] = []
