n, k = input().split(' ')
n = int(n)
k = int(k)

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
index = {}
for i in s:
    index[i] =[]

student = []
for i in range(n):
    grade, group = input().split(' ')
    grade = int(grade)
    student.append((grade, group))

for i in range(k):
    grade=input().split(' ')
    for j in range(k):
        index[s[j]].append(int(grade[j]))


# print(index)

import  math

def dg(num):
    # print(num)
    average = int(sum(num)/ len(num))
    new =[]
    for i in num:
        if math.fabs(i - average) <= 15:
            new.append(i)
    # print('new',new)
    if len(new) != len(num):
        return dg(new)
    else:
        return average

# print('''93 B
# 92 C
# 89 C
# 76 A
# 75 B
# 70 A''')

for i in range(k):
    # print(index[s[i]], s[i])
    index[s[i]] = dg(index[s[i]])

# print(index)

ans =[]
for grade, group in student:
    stu = grade * 0.6 + index[group] * 0.4
    # print(int(stu))
    ans.append([stu, group])

# ans = sorted(ans, key=)
for i in ans:
    print(int(i[0] + 0.5), end=' ')
    print(i[1])


