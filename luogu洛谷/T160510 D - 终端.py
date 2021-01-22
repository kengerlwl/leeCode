n = input()
n = int(n)

#文件的哈希系统
f = {}
ans = []
for i in range(n):
    s = input().split(' ')
    if s[0] =='touch':
        file = s[1]
        if file not in f:
            f[file] = i


    elif s[0] == 'rm':
        file = s[1]

        if file in f:
            f.__delitem__(file)
    elif s[0] == 'ls':
        l = []
        for j in f:
            l.append([f[j], j])
        l = sorted(l)
        for i in l:
            print(i[1])
            # ans.append(i[1])
        # print()
    elif s[0] == 'rename':
        file = s[1]
        new = s[2]
        if file not in f or new in f:
            ans
        elif file in f and new not in f:
                tmp = f[file]
                f.__delitem__(file)
                f[new] = tmp

# for i in ans:
#     print(i)