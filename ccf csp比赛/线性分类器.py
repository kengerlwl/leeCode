# θ0 +θ1x +θ2y =0
# y=(-θ0-θ1x)/θ2

p_list = []

def qurey(in_list):
    print(p_list)
    print(in_list)
    flag_gt = -1
    flag_lt = -1
    for i in p_list:
        if (in_list[0] + in_list[1] * int(i[0]) + in_list[2] * int(i[1])) >= 0:
            if flag_gt == -1:
                flag_gt = i[2]
                flag_lt = 'B' if i[2] == 'A' else 'A'
            if i[2] != flag_gt:
                print('No')
                return

        elif (in_list[0] + in_list[1] * int(i[0]) + in_list[2] * int(i[1])) < 0:
            if flag_lt == -1:
                flag_lt = i[2]
                flag_gt = 'B' if i[2] == 'A' else 'A'
            if i[2] != flag_lt:
                print('No')
                return
    print('Yes')

n,m = map(int,input().split())

for i in range(n):
    p_list.append(list(input().split()))

for i in range(m):
    qurey(list(map(int, input().split())))



