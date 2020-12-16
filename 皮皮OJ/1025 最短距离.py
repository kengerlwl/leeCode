cnt =1
while True:

    s  = input()
    if s =='\n':
        break

    mid = int(len(s) /2)
    flag = True
    for i in range(mid):
        if s[i] != s[len(s) - 1 - i]:
            flag =False
            break

    if flag:
        print('case{}: yes'.format(cnt))
    else:
        print('case{}: no'.format(cnt))
    cnt +=1