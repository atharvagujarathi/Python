def swap(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList




newList = [12, 54, 78, 87, 98]
print(swap(newList))    
