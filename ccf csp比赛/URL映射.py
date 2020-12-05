# url
import re

m, n = map(int, input().split())

rules = {}
rlist = {}
querys = []

for i in range(m):
    rule, name = input().split()
    rlist[rule] = rule.split("/")
    rules[rule] = name

print(rlist)


for i in range(n):
    query = input()
    q = query.split("/")
    find = False
    for rule in rules.keys():
        r = rlist[rule]
        if (len(q) >= len(r)):
            args = []
            match = 0
            RightPath = False
            for j in range(len(r)):
                if (q[j] == r[j]):
                    match += 1

                elif (q[j].isdigit() and r[j] == "<int>"):
                    args.append(str(int(q[j])))
                    match += 1

                elif (r[j] == "<str>"):
                    if (q[j] == ""):  # 加了这个判断就100分了 ?!空字符串对应<str>
                        break
                    args.append(q[j])
                    match += 1


                elif (r[j] == "<path>"):
                    args.append("/".join(q[len(r) - 1:]))
                    RightPath = True
                    match += 1

                else:
                    break

            if (match == len(r) and (len(q) == len(r) or RightPath)):
                print(rules[rule] + " " + " ".join(args))
                find = True
                break
        else:
            continue
    if (not find):
        print("404")