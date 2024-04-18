import heapq

def heapsort(iterable, comparator):
    h = []
    for value in iterable:
        heapq.heappush(h, (comparator(value), value))
    return [heapq.heappop(h)[1] for i in range(len(h))]

# 自定义比较函数
def my_comparison(value):
    return -value  # 以负数作为优先级，从大到小排序

# 使用自定义的比较函数进行堆排序
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0], my_comparison)
print(result)


