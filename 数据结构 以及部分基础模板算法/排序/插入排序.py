#插入排序
def insertSort(numList):
    newList =[numList[0]]
    for i in range(1,len(numList)):
        j =0
        # 是否再中间插入
        while j <= len(newList)-1:
            if numList[i] <= newList[j]:
                newList.insert(j, numList[i])
                break
            j+=1
        # 是否插入队尾
        if j == len(newList):
            newList.insert(j, numList[i])

    return newList


import random
num = [4,7,2,9,1,0,4,5,2]
a= insertSort(num)
print(a)




