n = input()
n = int(n)

#是否not 含有
def judge71(a):
    tmp = str(a)
    if tmp.count('7') ==0:
        return False
    else:
        return True


def judge72(a):
    if a % 7 ==0:
        return True
    else:
        return False

ans =[0 for i in range(4)]
now =0
count =0
i = 1
while count < n:
    now = i % 4
    if not judge72(i) and not judge71(i):
        # print(i)
        i+=1
        count+=1
    else:
        ans[now-1] +=1
        i+=1

# print(ans)
for i in ans:
    print(i)