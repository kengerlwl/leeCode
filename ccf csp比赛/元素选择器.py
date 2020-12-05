n, m  = input().split(' ')
n = int(n)
m = int(m)


class node:
    def __init__(self):
        self.parent =None
        self.children =[]
        self.deep = None  # 层级
        self.tag = None
        self.id = None
        self.index =None

    def show(self):
        print('.' * self.deep*2, end='')
        # print(self.id, end=' ')
        print(self.tag + ' ')
        for i in self.children:
            i.show()

now = input()
tag = None
id = None
s = now.split(' ')
if len(s) == 1:
    tag = s[0]
else:
    tag = s[0]
    id = s[1]



root  = node()
root.deep = 0
root.tag = tag
if id:
    root.id = id
nowNode = root
last = now
root.index =1



for i in range(n-1):
    now = input()
    tag = None
    id = None
    s= now.split(' ')
    if len(s) == 1:
        tag = s[0]
    else:
        tag = s[0]
        id = s[1]

    dot = now.count('.')
    lastDot = last.count('.')



    # next
    if dot - lastDot ==2:
        tmpNode = node()
        tmpNode.index = i+2
        tmpNode.tag = tag.replace('.','')
        if id:
            tmpNode.id = id
        tmpNode.deep = nowNode.deep+1
        tmpNode.parent = nowNode
        nowNode.children.append(tmpNode)
        nowNode = tmpNode
    # 同级
    elif dot - lastDot ==0:
        tmpNode = node()
        tmpNode.index = i+2
        tmpNode.tag = tag.replace('.','')
        if id:
            tmpNode.id = id
        tmpNode.deep = nowNode.deep
        tmpNode.parent = nowNode.parent
        nowNode.parent.children.append(tmpNode)
        nowNode = tmpNode
    else:
        dis = lastDot - dot
        while dis!=0:
            nowNode= nowNode.parent
            dis -=2
        tmpNode = node()
        tmpNode.index = i+2
        tmpNode.tag = tag.replace('.','')
        if id:
            tmpNode.id = id
        tmpNode.deep = nowNode.deep
        tmpNode.parent = nowNode
        nowNode.parent.children.append(tmpNode)
        nowNode = tmpNode


    last = now


# root.show()

def dfs_tag(node, tag):
    ans =0
    List =[]
    if node.tag.lower()  == tag.lower():
        ans +=1
        List.append(node.index)
    for i in node.children:
        num, l= dfs_tag(i, tag)
        ans += num
        List = List + l

    return ans, List


def dfs_id(node, tag):
    ans = 0
    List = []
    # print(node.tag)
    # print(node.id, tag)
    if node.id == tag:
        ans += 1
        List.append(node.index)
    for i in node.children:
        num, l = dfs_id(i, tag)
        ans += num
        List = List + l

    return ans, List


def judge(node, tags, now=0):

    List =[]
    # print(node.tag)
    if node.tag.lower() == tags[now].lower() and now < len(tags)-1:
        # print('chadsf')
        for i in node.children:
            a =judge(i, tags, now+1)
            List +=a
    elif node.tag.lower() == tags[now].lower() and now == len(tags)-1:
        return [node.index]
    else:
        return []

    return List


def dfs_tag_con(node, tags):
    List =[]
    if node.tag == tags[0]:
        a = judge(node,tags)
        # print(node.tag)
        # print(a)
        if len(a)!=0:
            List +=a

    for i in node.children:
        num, l = dfs_tag_con(i, tags)
        List = List + l

    return len(List), List

for i in range(m):
    s= input().split(' ')
    # print(s)
    if len(s) ==1:
        if s[0][0] =='#':
            num, l = dfs_id(root, s[0])

        else:
            num, l =dfs_tag(root, s[0])

        print(num, end=' ')
        for i in l:
            print(i, end=' ')
        print()

    else:
        num, l = dfs_tag_con(root, s)
        print(num, end=' ')
        for i in l:
            print(i, end=' ')
        print()