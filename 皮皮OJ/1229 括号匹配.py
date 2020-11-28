
# 一个典型的适应oj输入输出
s = input()
while s!= '':
    # print(s)

    stack=[]
    ans = True
    for i in range(len(s)):
        if i <1:
            stack.append(s[i])
            continue
        if s[i] ==')':
            if stack[len(stack) -1]== '(':
                a = stack.pop()
            else:
                stack.append(s[i])
        elif s[i] ==']':
            if stack[len(stack) -1]== '[':
                a = stack.pop()
            else:
                stack.append(s[i])
        elif s[i] == '}':
            if stack[len(stack) - 1] == '{':
                a = stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    # print(stack)

    if stack ==[]:
        print('yes')
    else:
        print('no')

    s = input()