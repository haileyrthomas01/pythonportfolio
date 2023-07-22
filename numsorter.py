myList = [23, -5, 66, 2, -10, 20, 79, 100, 11]
sortList = []

while myList:
    minNum = myList[0]
    for x in myList:
        if x < minNum:
            minNum = x
    sortList.append(minNum)
    myList.remove(minNum)

print(sortList)