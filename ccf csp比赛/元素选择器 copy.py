
# 输入
n, m = map(int, input().split())
doc = []
sel = []
# 结构化文档内容
for i in range(n):
    doc.append(input())
# 带查询的选择器
for i in range(m):
    sel.append(input())

# 解析文档结构
cons = []
for i in range(n):
    level = doc[i].count('.') // 2
    tag = ""
    tid = ""
    if (len(doc[i].split()) == 1):
        tag = doc[i][level * 2:]
    else:
        left, right = doc[i].split()
        tag = left[level * 2:]  # 标签大小写不敏感
        tid = right  # id大小写敏感
    pline = -1;
    for j in range(i - 1, 0 - 1, -1):
        if (cons[j]["level"] == level - 1):
            pline = j + 1;
            break;
    cons.append({"tag": tag, "id": tid, "level": level, "pline": pline})  # 将信息存为字典添加到列表中

# 元素选择器选择
collection = []  # 结果保存列表
for i in range(m):
    collection.append([])
    if (len(sel[i].split()) == 1):  # 选择器不含空格
        if (sel[i][0] != '#'):  # 标签选择器
            for j in range(n):
                if (cons[j]["tag"].lower() == sel[i].lower()):  # 标签大小写不敏感
                    collection[i].append(j + 1)
        else:  # id选择器
            for j in range(n):
                if (cons[j]["id"] == sel[i]):  # id大小写敏感
                    collection[i].append(j + 1)
    else:  # 后代选择器

        p = sel[i].split()
        for j in range(n):
            parent = j + 1
            k = len(p) - 1
            while k >= 0:  # 从后向前迭代检查是否匹配
                match = False
                if (p[k][0] != '#'):
                    if (cons[parent - 1]["tag"].lower() == p[k].lower()):
                        match = True
                    else:
                        if (parent == j + 1 and k == len(p) - 1):  # 第一次必须匹配上不然直接退出
                            break
                else:
                    if (cons[parent - 1]["id"] == p[k]):
                        match = True
                    else:
                        if (parent == j + 1 and k == len(p) - 1):
                            break
                if (match):
                    k -= 1
                    if (k < 0):  # 匹配成功
                        collection[i].append(j + 1)
                        break
                if (cons[parent - 1]["pline"] == -1):  # 没有父节点了仍未匹配成功即匹配失败
                    break  # 匹配失败退出
                parent = cons[parent - 1]["pline"]  # 取父节点继续检查匹配

# 输出
for x in collection:
    print(len(x), " ".join(map(str, x)))


11 7
html
..head
....title
..body
....h1
....p #subtitle
....div #main
......h2
......p #one
......div
........p #two
p
#Subtitle
h3
div p
div div p
html
root