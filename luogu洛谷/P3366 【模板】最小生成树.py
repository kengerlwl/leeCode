n , m  = input().split(' ')
n = int(n)


import heapq

# print(n)
m = int(m)
edges =[]
for i in range(m):
    s  = input().split(' ')
    edges.append(( int(s[0]),int(s[1]),int(s[2]) ))

adj = {}  # 邻接表
for i in range(1, n + 1):
    adj[i] = {}

for u, v, w in edges:
    if v in adj and u in adj[v]:
        if   w < adj[u][v]:
            adj[u][v] = w
            adj[v][u] = w
    else:
        adj[u][v] = w
        adj[v][u] = w
arrive ={}


hq = []
# 以 1 开始
start = 1
arrive[start] = True
cnt ={}  # 统计在队列中出现次数
for i in range(1, n+1):
    cnt[i] =0


for i in adj[start]:
    if i not in arrive:
        heapq.heappush(hq, [adj[start][i], i])
        cnt[i] +=1

# print(hq)
sum =0
count =0
# print(adj[2][5])


while hq:
    # print(hq)
    w, v = heapq.heappop(hq)
    if v not in arrive:
        # print(v,w)

        arrive[v] = True
        sum +=w
        count +=1
        for i in adj[v]:
            if i not in arrive and cnt[i] < n:
                cnt[i] +=1
                heapq.heappush(hq, [adj[v][i], i])



if count == n - 1:
    print(sum)
else:
    print('orz')