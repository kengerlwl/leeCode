class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        class point():
            def __init__(self):
                self.x = None
                self.y= None
            def tostrint(self):
                print(self.x, self.y)

        high = len(board)
        width = len(board[0])

        queue = []

        il =[0, high-1]
        for j in range(width):
            for i in il:
                if board[i][j] == 'O':
                    p = point()
                    p.x=j
                    p.y=i

                    queue.append(p)
        jl = [0, width-1]
        for i in range(1, high-1):
            for j in jl:
                if board[i][j] == 'O':
                    p = point()
                    p.x = j
                    p.y = i

                    queue.append(p)
        for i in queue:
            i.tostrint()

        #以上完成了基本得边界检测
        import copy
        boardNew = copy.deepcopy(board)

        #代表是否来过
        res=[]
        for i in range(high):
            tmp =[]
            for j in range(width):
                tmp.append(False)
                boardNew[i][j] = 'X'
            res.append(tmp)
        # print(res)


        while len(queue) !=0:

            top = queue.pop()
            i = top.y
            j = top.x
            boardNew[i][j] = 'O'
            res[i][j] = True

            il = [1, -1]
            jl = [1, -1]
            #向上下左右四个方向进行遍历
            for m in il:
                for n in jl:
                    tmpi = i + m
                    tmpj = j + n

                    if tmpi <0 or tmpi >= high or tmpj <0 or tmpj >= width:
                        continue

                    if res[tmpi][tmpj] and (board[tmpj][tmpj] == 'O'):
                        p = point()
                        p.x = tmpj
                        p.y = tmpi
                        queue.append(p)
        print(boardNew)
        return  boardNew










Solution.solve(None,[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])