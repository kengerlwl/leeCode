class Solution:
    def maxProbability(self, n, edges, succProb, start, end) :
        if not edges or not edges[0]: return 0

        # 构造节点邻接表, 邻接以及概率
        from collections import defaultdict
        st_maps = defaultdict(list)
        for i, (s, e) in enumerate(edges):
            st_maps[s].append((e, succProb[i]))
            st_maps[e].append((s, succProb[i]))

        print(st_maps)


        numPro ={}
        numPro[start] = 1
        for i in range(n):
            if i != start:
                numPro[i] = 0  # 除了到达其本身，其他都为0

        queue = []
        queue.append(start)

        #某个节点是否遍历过
        flag =[]
        for i in range(n):
            flag.append(False)

        while queue:
            top = queue.pop()

            for i in st_maps[top]:
                # print(i)
                pro = numPro[top]
                pro = pro * i[1]
                if numPro[i[0]] < pro: #如果新路径更优
                    numPro[i[0]] = pro
                    queue.append(i[0])


        print(numPro[end])




Solution.maxProbability(None,n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2

)