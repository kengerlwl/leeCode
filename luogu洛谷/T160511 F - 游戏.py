n = input()
n = int(n)

c1, c2 = input().split(' ')

c1  = int(c1)
c2 = int(c2)

s  = input().split(' ')
List  = []
for i in s:
    List.append(int(i))

#
# for i in List:
#     print(bin(i))

def count(a):
    s = str(bin(a))
    # print(s.count('1'))
    return  s.count('1')

length  = len(List)

adj = {}
for i in range(n):
    adj[i] = {}

f = c1 < c2
edges = []
for i in range(0, length):
    for j in range(i+1, length):
        a  = List[i]
        b = List[j]
        if count(a^b) ==1:
            # adj[i][j] = c1
            # adj[j][i] = c1
            edges.append([i, j, c1])
            edges.append([j, i, c1])


            if f:
                break
        elif count(a^b) >1:
            # adj[i][j] = c2
            # adj[j][i] = c2
            edges.append([i, j, c2])
            edges.append([j, i, c2])

            if not f:
                break
import heapq


# 并查集
class BQSet():
    def __init__(self):
        self.f = {}
        # #init
        # for i in range(10):
        #     f[i] = i

    def getFather(self, origin):
        a = origin
        while self.f[a] != a:
            a = self.f[a]
        self.f[origin] = a
        return a

    # 只需要看a， b 是否 有共同父节点
    def judge(self, a, b):
        a = self.getFather(a)
        b = self.getFather(b)

        if self.f[a] == self.f[b]:
            return True
        else:
            return False

    def Union(self, source, a):
        a = self.getFather(a)
        sF = self.getFather(source)
        self.f[a] = sF


#  Kruskal 关键是判断是不是同一个集合里面


def kruskal(edges):
    bq = BQSet()

    # 初始化并查集
    for i in range(0, n + 1):
        bq.f[i] = i

    # 先进行排序
    edges = sorted(edges, key=lambda x: x[2])
    # print(edges)
    arried = {}
    # finalE =[]
    sum = 0
    count = 0
    for u, v, w in edges:
        if bq.judge(u, v):
            pass
        else:  # 如果边不在同一个集合，就加入
            bq.Union(u, v)
            sum += w
            count += 1

    if count == n - 1:
        print(sum)
    else:
        print('orz')


# print(count)



kruskal(edges)