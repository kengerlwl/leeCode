x = 127
i = x
while i > 0:
    print(bin(i))
    i = (i-1) & x
    # print(i)
