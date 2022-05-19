import ReadData as rd

# =========================== Forward Pass ===========================
# znajdujemy najwczesniejszy start (ES) i najwczesniejszy koniec (EF)

for i in rd.tasks:
    if ('-1' in rd.tasks[i]['predecessors']):
        rd.tasks[i]['ES'] = 0
        rd.tasks[i]['EF'] = (rd.tasks[i]['duration'])
    else:
        predEFList = list()
        for j in rd.tasks[i]['predecessors']:
            predEFList.append(int(rd.tasks['T' + j]['EF']))
        rd.tasks[i]['ES'] = max(predEFList)
        rd.tasks[i]['EF'] = int(rd.tasks[i]['ES']) + int(rd.tasks[i]['duration'])

# =========================== Backward Pass ===========================
# znajdujemy najpozniejszy start (LS) i najpozniejszy koniec (LF)

max = 0
for i in range(1, len(rd.tasks) + 1):
    if (max < int(rd.tasks['T' + str(i)]['EF'])):
        max = int(rd.tasks['T' + str(i)]['EF'])

actualSuccs = list()
actualSuccs.append("0")
for i in rd.tasks:
    actualSuccs.append(rd.tasks[i]['predecessors'])

for succ in range(len(actualSuccs)):
    for node in actualSuccs[succ]:
        if (int(node) > 0):
            rd.tasks['T' + node]['successors'].append(succ)

tempKeys = list()
for element in rd.tasks.keys():
    tempKeys.append(element)

reversedKeys = list()
while len(tempKeys) > 0:
    reversedKeys.append(tempKeys.pop())

for i in reversedKeys:
    if not rd.tasks[i]['successors']:
        rd.tasks[i]['LF'] = max
        rd.tasks[i]['LS'] = int(rd.tasks[i]['LF']) - int(rd.tasks[i]['duration'])
    else:
        succLSList = list()
        for j in rd.tasks[i]['successors']:
            succLSList.append(int(rd.tasks['T' + str(j)]['LS']))
        rd.tasks[i]['LF'] = min(succLSList)
        rd.tasks[i]['LS'] = int(rd.tasks[i]['LF']) - int(rd.tasks[i]['duration'])

# ================================ END ================================
# znalezienie wezlow bedacych na sciezce krytycznej i print

for i in rd.tasks:
    rd.tasks[i]['float'] = rd.tasks[i]['ES'] - rd.tasks[i]['LS']

print('name\tduration\tES\tEF\tLS\tLF\tisCritical')
for task in rd.tasks:
    if (rd.tasks[task]['float'] == 0):
        rd.tasks[task]['isCritical'] = True
    print(str(rd.tasks[task]['name']) + '\t\t' + str(rd.tasks[task]['duration']) + '\t\t\t' + str(
        rd.tasks[task]['ES']) + '\t' + str(rd.tasks[task]['EF']) + '\t' + str(rd.tasks[task]['LS']) + '\t' + str(
        rd.tasks[task]['LF']) + '\t' + str(rd.tasks[task]['isCritical']))

print("\nWęzły tworzące ścieżkę krytyczną: ")
for task in rd.tasks:
    if (rd.tasks[task]['isCritical'] == True):
        print(str(rd.tasks[task]['name']), end=", ")
print()