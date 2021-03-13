def createListArea():
    file = open('area.txt', encoding='UTF-8')
    areaList = []
    for i in file:
        i = i.split('\n')
        areaList.append(i[0])
        areaList.sort()
    return areaList

