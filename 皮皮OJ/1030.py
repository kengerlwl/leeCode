# 4 5 *
s = input()

while True:
    if s =="" or s =='\n':
        break
    s = s.split(' ')
    # change data
    m = s[0]
    m = int(m)
    n = int(s[1])
    c  = s[2]

    print(c*n)

    for i in range(m-2):
        print(' '*(i+1), end=c)
        print(' '*(n-2),end=c)
        print(' ')
    if m >=2:
        print(' ' * (m - 1), end='')
        print(c*n, end='')
        print()
    s = input()
