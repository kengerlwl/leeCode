n = input()
n = int(n)
def judge(num):
    s = str((num))
    Sum =0
    for i in s:
        Sum += int(i)
        if Sum >9:
            return False
    if Sum ==9:
        return True
    else:
        return False
ans =0
i =1
while i < n+1:
    if i %3 ==0:
        if judge(i):
            ans+=1

    i +=1



print(ans)
