#二分插入排序
def dichotomy(numList):
    newList =[numList[0]]
    for i in range(1,len(numList)):
        l = 0
        r = len(newList)
        #二分搜索需要插入得地方
        while l < r:
            # print(newList,i, l,r)
            mid = (l +r) //2

            if  numList[i] > newList[mid]:
                l = mid +1
            # elif  numList[i] <= newList[mid]:
            else:
                r = mid
        if l == r:
            newList.insert(l, numList[i])


    return newList

import random
num = [5,1,1,2,0,0]
a= dichotomy(num)
print(a)

