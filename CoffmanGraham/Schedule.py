import ReadData as rd
import CoffmanGraham as cg

def printMachines(m1, m2):
    if len(m1) < len(m2):
        for i in range(len(m2) - len(m1)):
            m1.append([])
    elif len(m2) < len(m1):
        for i in range(len(m1) - len(m2)):
            m2.append([])

    print('M1: ', end=' | ')
    for i in m1:
        if not i:
            print('--', end=' | ')
        else:
            print('T' + str(i), end=" | ")
    print('\nM2: ', end=' | ')
    for i in m2:
        if not i:
            print('--', end=' | ')
        else:
            print('T' + str(i), end=" | ")

def checkIfAllPredecessorsAreFinished(predecessors, finishedTasks):
    i = 0
    for pred in predecessors:
        if int(pred) in finishedTasks:
            i += 1
    if (i == len(predecessors) and i <= len(finishedTasks)):
        return True
    else:
        return False

def appendToMachine(machine, task, tasks, allTasks, finishedTasks):
    if not tasks['T' + str(task)]['predecessors']:
        machine.append(task)
        if task in allTasks:
            allTasks.remove(task)
    elif checkIfAllPredecessorsAreFinished(tasks['T' + str(task)]['predecessors'], finishedTasks):
        machine.append(task)
        if task in allTasks:
            allTasks.remove(task)
    else:
        machine.append([])

def getAmountOfTasks(machine):
    counter = 0
    for i in machine:
        if i:
            counter += 1
    return counter

def schedule(listL, tasks):
    m1 = list()
    m2 = list()
    allTasks = listL.copy()
    finishedTasks = list()
    while len(allTasks) > 0:
        for i in range(len(listL)):
            for j in m1:
                finishedTasks.append(j)
            for j in m2:
                finishedTasks.append(j)
            if i == 0:
                appendToMachine(m1, listL[i], tasks, allTasks, finishedTasks)
            else:
                if len(m1) < len(m2) and not listL[i] in tasks['T' + str(listL[i-1])]['successors']:
                    appendToMachine(m1, listL[i], tasks, allTasks, finishedTasks)
                elif len(m1) > len(m2) and not listL[i] in tasks['T' + str(listL[i-1])]['successors']:
                    appendToMachine(m2, listL[i], tasks, allTasks, finishedTasks)
                else:
                    appendToMachine(m1, listL[i], tasks, allTasks, finishedTasks)

            if len(m2) < i-getAmountOfTasks(m2):
                m2.append([])
            if len(m1) < i-getAmountOfTasks(m1):
                m1.append([])
            finishedTasks.clear()


    print('-----------------------------------')
    print('Harmonogram:')
    printMachines(m1, m2)
    print('\nCmax = ', end='')
    print(len(m1))

schedule(cg.coffmanGraham(rd.tasks), rd.tasks)