height = input().split(' ')
def change(numList):
    ans =[]
    for i in numList:
        ans.append(int(i))
    return ans
height = change(height)

me = int(input())
ans =0
for i in height:
    if me + 30 >= i:
        ans +=1


print(ans)