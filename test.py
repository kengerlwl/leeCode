# import heapq
# import random
# q =[]
# for i in range(10):
#     heapq.heappush(q, random.randint(1,10))
#     print(q)
# print(q)
import heapq

nums = [14, 20, 5, 28, 1, 21, 16, 22, 17, 28]
b = heapq.heappop(nums)
print(b)
print(nums)
# [1, 5, 14]