arr = [i+1 for i in range(5)]


visit = [True for i in range(len(arr))]
temp = ["" for x in range(0, len(arr))]
# 回溯记录

def dfs(position):
    if position == len(arr):
        print(temp)
        return None

    for index in range(0, len(arr)):
        if visit[index] == True:
            temp[position] = arr[index]
            visit[index] = False
            dfs(position + 1)
            visit[index] = True


dfs(0)