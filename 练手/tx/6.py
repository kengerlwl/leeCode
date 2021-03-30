while True:
    try:
        n = input()
    except:
        break
    n = int(n)

    list = {}
    for i in range(n):
        num = input()
        num = int(num)

        list[num] = True

    index = sorted(list)

    for i in index:
        print(i)

