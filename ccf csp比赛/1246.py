n = int(input())
s =input()

import  math

dight =1
StrOfDig = ''
for i in range(n):
    Stmp = str(dight)
    ans = ""
    for j in Stmp:
        j = int(j)
        j = math.pow(2, j)
        ans = ans + str(int(j))
    dight = ans
    if i == (n-1):
        StrOfDig = ans

length = len(s)
count =0
for i in range(len(StrOfDig)):
    if i + length > len(StrOfDig):
        continue
    subS = StrOfDig[i:i +length]
    if subS == s:
        count +=1
print(count % 998244353)
