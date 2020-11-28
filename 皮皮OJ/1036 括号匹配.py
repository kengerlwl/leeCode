
# 一个典型的适应oj输入输出
while True:

    s = input()
    if s == '':
        break

    # print(s)

    stack=[]
    ans =[]
    for i in range(len(s)):
        if s[i] ==')':
            if stack[len(stack) -1][1] == '(':
                a = stack.pop()
                ans.append([a[0] +1, i+1])
            else:
                stack.append((i, s[i]))
        else:
            stack.append((i,s[i]))

    # print(ans)
    ans = sorted(ans)
    for i in ans:
        for j in i:
            print(j, end=' ')
        print('')
