#
# #初始化数组
# dp = [0 for i in range(5)]
# [0, 0, 0, 0, 0]





# #定义二维数组
# dp = [[0 for i in range(5)] for i in range(3)]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]







# # 排序数据结构
# my_dict = {"a":"2", "c":"5", "b":"1"}
#
# result = sorted(my_dict)
# #默认对dict排序，不指定key参数,会默认对dict的key值进行比较排序
# #result输出: ['a', 'b', 'c']
#
# result2 = sorted(my_dict, key=lambda x:my_dict[x])
# #指定key参数，根据dict的value排序
# #result2输出:['b', 'a', 'c']

# sorted()的reverse参数接受False 或者True 表示是否逆序

# 使用比较函数
# import functools
# def cmp(a, b):
#     if a > b:
#         return -1
#     elif a < b:
#         return 1
#     else:
#         return 0
#
#
# nums = [1, 2, 3, 4, 5, 6]
# sorted_nums = sorted(nums, key=functools.cmp_to_key(cmp))
#
# #[6, 5, 4, 3, 2, 1]






# # 有序数据结构
# from sortedcontainers import SortedList
# sl = SortedList(['e', 'a', 'c', 'd', 'b'])
# print(sl)


# from sortedcontainers import SortedDict
# sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
# sd['a'] =10   # 更新
# sd['d'] =0    # 新增
# sd.pop('a')   # 删除
# print(sd)







#
# # 正常先进先出队列   leecode不支持
# import queue
#
# q=queue.Queue()    #如果不设置长度,默认为无限长
# q.put(123)
# q.put(456)
# q.put(789)
# q.put(100)
# q.put(111)
# q.put(233)






# 后进先出队列
# q = queue.LifoQueue()
# q.put(12)
# q.put(34)
# print(q.get())


#
# # 数组
# q = []
# q.append(1)
# q.append(2)
# q.append(3)
# a = q.pop()
# a =q.remove(1)
#
# print(a)
# print(q)
#






# # 优先级队列

#
# import heapq as  hq
# #向堆中插入元素，heapq会维护列表heap中的元素保持堆的性质
# h = []
# hq.heappush(h, [5, 'write code'])
# hq.heappush(h, [7, 'release product'])
# hq.heappush(h, [1, 'write spec'])
# hq.heappush(h, [3, 'create tests'])


# laptops = [
#     {'name': 'ThinkPad', 'amount': 100, 'price': 91.1},
#     {'name': 'Mac', 'amount': 50, 'price': 543.22},
#     {'name': 'Surface', 'amount': 200, 'price': 21.09},
#     {'name': 'Alienware', 'amount': 35, 'price': 31.75},
#     {'name': 'Lenovo', 'amount': 45, 'price': 16.35},
#     {'name': 'Huawei', 'amount': 75, 'price': 115.65}
# ]
#
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])



# print(h)
#
# a = hq.heappop(h)
# print(a)
#
# b = hq.nlargest(2, h,lambda s:s[1])
# print(b)










# 哈希表
#判断是否在表里面
# A = {1,2,3,4}
# a =1
# flag = a in A
# print(flag)


