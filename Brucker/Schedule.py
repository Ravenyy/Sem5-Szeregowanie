import ReadData as rd
import Brucker as br

def printMachines(m1, m2, m3):
    print('M1: ', end=' | ')
    for i in m1:
        if not i:
            print('--', end=' | ')
        else:
            print(str(i), end=" | ")
    print('\nM2: ', end=' | ')
    for i in m2:
        if not i:
            print('--', end=' | ')
        else:
            print(str(i), end=" | ")
    print('\nM3: ', end=' | ')
    for i in m3:
        if not i:
            print('--', end=' | ')
        else:
            print(str(i), end=" | ")

def checkIfAllPredecessorsAreFinished(predecessors, finishedTasks):
    i = 0
    for pred in predecessors:
        if int(pred) in finishedTasks:
            i += 1
    if (i == len(predecessors) and i <= len(finishedTasks)):
        return True
    else:
        return False

def appendToMachine(machine, i, tasks, allTasks, finishedTasks):
    if not tasks['T' + str(i)]['predecessors']:
        machine.append(tasks['T' + str(i)]['name'])
        if i in allTasks:
            allTasks.remove(tasks['T' + str(i)]['name'])
    elif checkIfAllPredecessorsAreFinished(tasks['T' + str(i)]['predecessors'], finishedTasks):
        machine.append(tasks['T' + str(i)]['name'])
        if i in allTasks:
            allTasks.remove(tasks['T' + str(i)]['name'])
    else:
        machine.append([])

def schedule(tasks):
    m1 = list()
    m2 = list()
    m3 = list()
    allTasks = list()
    for i in tasks:
        allTasks.append(tasks[i]['name'])
    finishedTasks = list()
    while len(allTasks) > 0:
        for i in tasks:
            if i == 1:
                appendToMachine(m1, i, tasks, allTasks, finishedTasks)
                if tasks['T' + str(i)]['name'] in allTasks:
                    allTasks.remove(tasks['T' + str(i)]['name'])
            else:

                allTasks.remove(tasks['T' + str(i)]['name'])

    printMachines(m1, m2, m3)