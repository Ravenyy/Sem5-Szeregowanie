import ReadData as rd

def findSuccessors(tasks):
    actualSuccs = list()
    actualSuccs.append("0")
    for i in tasks:
        actualSuccs.append(tasks[i]['predecessors'])

    for succ in range(len(actualSuccs)):
        for node in actualSuccs[succ]:
            if (int(node) > 0):
                rd.tasks['T' + node]['successors'].append(succ)

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


def findNodesWithoutSuccessors(tasks):
    noSuccessors = list()
    for i in range(1, len(tasks) + 1):
        if not tasks['T' + str(i)]['successors']:
            noSuccessors.insert(0, i)
    return noSuccessors


def removeLabeled(idList, listL):
    for i in idList:
        for j in listL:
            if i == j:
                idList.remove(i)


def checkIfAllSuccessorsAreLabeled(successors, listL):
    i = 0
    for succ in successors:
        if succ in listL:
            i += 1
    if (i == len(successors) and i <= len(listL)):
        return True
    else:
        return False

def findLexMinList(listA, s_list):
    lexMin = len(s_list) + 1
    indexOfLexMinList = -1
    for i in listA:
        s_list['T' + str(i)]['successors'].reverse()
        if s_list['T' + str(i)]['successors'][0] < lexMin:
            lexMin = s_list['T' + str(i)]['successors'][0]
            indexOfLexMinList = i
    return indexOfLexMinList

def coffmanGraham(tasks):
    findSuccessors(tasks)
    idList = list()
    listA = list()
    listL = list()
    counter = len(tasks)
    iterCounter = 1

    while counter > 0:
        idList.append(int(tasks['T' + str(counter)]['id']))
        counter -= 1

    for i in range(len(findNodesWithoutSuccessors(tasks))):
        listL.append(findNodesWithoutSuccessors(tasks)[i])
        removeLabeled(idList, listL)

    while len(idList) > 0:
        for i in idList:
            if checkIfAllSuccessorsAreLabeled(tasks['T' + str(i)]['successors'], listL):
                s_list = tasks['T' + str(i)]['successors'].copy()
                if(s_list and len(s_list) > 1):
                    if s_list[0] < s_list[1]:
                        s_list.reverse()
                print('s_list(' + str(i) + ')', end=': ')
                print(s_list)
                listA.insert(0, i)
                # listA.append(i)

        print('Aktualna iteracja', end=': ')
        print(iterCounter)
        print('Lista A', end=': ')
        print(listA)
        print('Lista L', end=': ')
        print(listL)
        print('Lista nodow \'niegotowych\'', end=': ')
        print(idList)
        print('-----------------------------------')

        listL.insert(0, findLexMinList(listA, tasks))
        listA.clear()
        removeLabeled(idList, listL)
        iterCounter -=- 1

    print('Lista L po zakończeniu wszystkich iteracji', end=': ')
    print(listL)
    return listL