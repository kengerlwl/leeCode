n = input()
n = int(n)
s = input().split(' ')
numList =[]
for i in s:
    numList.append(int(i))

newList =[numList[0], numList[1]]
minV = min(newList)
maxV = max(newList)
sumOfAll = sum(newList)
for i in range(2,n):
    sumOfAll +=numList[i]
    maxV = max(maxV, numList[i])
    minV = min(minV, numList[i])

    ans =  sumOfAll - maxV - minV
    ans = ans / (i-1)
    print('%.2f'%ans)\