import ReadData as rd

def findRoot(tasks):
    for i in range(1, len(tasks) + 1):
        if not tasks['T' + str(i)]['successors']:
            return i

def findFirstNodes(tasks):
    firstNodes = list()
    for i in range(1, len(tasks) + 1):
        if not tasks['T' + str(i)]['predecessors']:
            firstNodes.append(i)
    return firstNodes

def getBranch(task, tasks, nextTask, branch):
    if tasks[task]['successors']:
        if not tasks['T' + str(nextTask)]['successors']:
            branch.append(nextTask)
            return branch
        else:
            branch.append(nextTask)
            nextTask = tasks['T' + str(nextTask)]['successors'][0]
            return getBranch(task, tasks, nextTask, branch)
    else:
        return []

def setD(task, tasks, branch):
    taskSuccessor = tasks[task]['successors'][0]
    while not tasks[task]['d']:
        for i in branch:
            if not i == branch[len(branch) - 1]:
                successor = tasks['T' + str(i)]['successors'][0]
                if tasks['T' + str(successor)]['d']:
                    tasks['T' + str(i)]['d']\
                        .append(max((1+int(tasks['T' + str(successor)]['d'][0])),
                                    (1-int(tasks['T' + str(i)]['duration']))))
        if tasks['T' + str(taskSuccessor)]['d']:
            tasks[task]['d']\
                .append(max((1+int(tasks['T' + str(taskSuccessor)]['d'][0])),
                            (1-int(tasks[task]['duration']))))

def getNotFirstNodes(tasks):
    notFirstNodes = list()
    for i in range(1, len(tasks)+1):
        if tasks['T' + str(i)]['predecessors']:
            notFirstNodes.append(i)
    return notFirstNodes

def getC(tasks, machines):
    m = 3
    root = findRoot(tasks)
    finishedTasks = list()
    machines.append(list())
    firstNodes = findFirstNodes(tasks)
    machineCounter = 0
    otherTasks = findTasksToAppend(tasks, firstNodes, root)
    for i in range(len(firstNodes)):
        if i < m:
            machines[machineCounter].append(firstNodes[i])
            finishedTasks.append(firstNodes[i])
        elif len(machines[machineCounter]) == m:
            machineCounter += 1
            machines.append(list())
            machines[machineCounter].append(firstNodes[i])
            finishedTasks.append(firstNodes[i])
        else:
            machines[machineCounter].append(firstNodes[i])
            finishedTasks.append(firstNodes[i])

    while len(otherTasks) > 0:
        appended = list()
        for i in range(len(otherTasks)):
            if len(machines[machineCounter]) < m and len(machines) == len(firstNodes) % m:
                machines[machineCounter].append(otherTasks[i][0])
                finishedTasks.append(otherTasks[i][0])
                appended.append(otherTasks[i])
            elif len(machines[machineCounter]) < m \
                    and int(tasks['T' + str(otherTasks[i][0])]['predecessors'][0]) in machines[machineCounter]:
                machines[machineCounter].append([])
            elif len(machines[machineCounter]) == m \
                    and int(tasks['T' + str(otherTasks[i][0])]['predecessors'][0]) in finishedTasks:
                machineCounter += 1
                machines.append(list())
                machines[machineCounter].append(otherTasks[i][0])
                finishedTasks.append(otherTasks[i][0])
                appended.append(otherTasks[i])
            elif int(tasks['T' + str(otherTasks[i][0])]['predecessors'][0]) in finishedTasks:
                machines[machineCounter].append(otherTasks[i][0])
                finishedTasks.append(otherTasks[i][0])
                appended.append(otherTasks[i])
        for i in appended:
            otherTasks.remove(i)
    machines.append(list())
    machines[len(machines)-1].append(root)

def findTasksToAppend(tasks, firstNodes, root):
    tasksList = list()
    tempList = list()
    sortedList = list()
    for i in tasks:
        if not int(tasks[i]['id']) in firstNodes and int(tasks[i]['id']) != root:
            tempList.append(int(tasks[i]['id']))
    for i in range(1, len(tasks) + 1):
        if i in tempList:
            tasksList.append([i, tasks['T' + str(i)]['d'][0]])
    while len(tasksList) > 0:
        current = [0, 0]
        for i in range(len(tasksList)):
            if current[1] > tasksList[i][1]:
                current = [tasksList[i][0], tasksList[i][1]]
        if current != [0, 0]:
            sortedList.append(current)
            tasksList.remove(current)
    sortedList.reverse()
    return sortedList

def brucker(tasks):
    rootNode = findRoot(tasks)
    tasks['T' + str(rootNode)]['d'].append(1 - int(tasks['T' + str(rootNode)]['duration']))
    for i in findFirstNodes(tasks):
        setD('T' + str(i), tasks, getBranch('T' + str(i), tasks, tasks['T' + str(i)]['successors'][0], []))


def createMachinesLists(machines, m1, m2, m3):
    for j in range(len(machines)):
        if len(machines[j]) < 3:
            for i in range(3 - len(machines[j])):
                machines[j].append([])
    for j in range(len(machines)):
        m1.append(machines[j][0])
        m2.append(machines[j][1])
        m3.append(machines[j][2])

def printSchedule(tasks):
    machines = list()
    m1 = list()
    m2 = list()
    m3 = list()
    brucker(tasks)
    getC(tasks, machines)
    createMachinesLists(machines, m1, m2, m3)

    print('\nM1', end=' | ')
    for i in m1:
        if i:
            print(i, end=' | ')
        else:
            print('--', end=' | ')
    print('\nM2', end=' | ')
    for i in m2:
        if i:
            print(i, end=' | ')
        else:
            print('--', end=' | ')
    print('\nM3', end=' | ')
    for i in m3:
        if i:
            print(i, end=' | ')
        else:
            print('--', end=' | ')

    for i in range(len(m1)):
        if m1[i] != []:
            tasks['T' + str(m1[i])]['L'].append((i+1) - int(tasks['T' + str(m1[i])]['duration']))
            tasks['T' + str(m1[i])]['start'].append(i)
            tasks['T' + str(m1[i])]['end'].append(i+1)
    for i in range(len(m2)):
        if m2[i] != []:
            tasks['T' + str(m2[i])]['L'].append((i+1) - int(tasks['T' + str(m2[i])]['duration']))
            tasks['T' + str(m2[i])]['start'].append(i)
            tasks['T' + str(m2[i])]['end'].append(i+1)
    for i in range(len(m3)):
        if m3[i] != []:
            tasks['T' + str(m3[i])]['L'].append((i+1) - int(tasks['T' + str(m3[i])]['duration']))
            tasks['T' + str(m3[i])]['start'].append(i)
            tasks['T' + str(m3[i])]['end'].append(i+1)

    print('\n')
    Llist = list()
    for i in tasks:
        Llist.append(tasks[i]['L'][0])
        print()
        print(tasks[i]['name'], end=', start: ')
        print(tasks[i]['start'][0], end=', end: ')
        print(tasks[i]['end'][0], end=', d: ')
        print(tasks[i]['duration'], end=', d')
        print(tasks[i]['id'], end='*: ')
        print(tasks[i]['d'][0], end=', L: ')
        print(tasks[i]['L'][0], end='.')

    print('\n\nLmax = ', end='')
    print(max(Llist))

printSchedule(rd.tasks)