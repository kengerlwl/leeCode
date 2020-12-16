n = input()
n = int(n)

m = input()
m = str(m)

def MyReserve(s):
    new = ''
    for i in s:
        new = i + new
    return new

def judge(s):
    f = True
    for i in range(len(s) //2):
        if s[i] != s[len(s)-1 -i]:
            f = False

    return f

#将10 进制转化为N进制
def TentoN(num, N):
    num = int(num)
    ans =[]

    while num !=0:
        rest = num % N
        num = num // N
        ans.append(rest)

    ans.reverse()
    return ans


# 将N进制转化为10进制
def NtoTen(num, N):
    ans =0
    num = str(num)
    for i in num:
        ans= ans * N + int(i)

    return ans


def cal(a, b, N):
    a = NtoTen(a, N)
    b = NtoTen(b, N)

    ans =  a+b

    ans = TentoN(ans, N)

    a = ''
    for i in ans:
        a += str(i)
    return a




count = 0
while not judge(m) and count < 20:
    m = cal(m, MyReserve(m), n)
    m = str(m)
    count+=1

print('STEP={}'.format(count))