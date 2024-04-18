## 常见技巧



### lambda表达式

```
lambda arguments: expression
```

例如 :

```
add = lambda x, y: x + y
print(add(3, 5))  # 输出 8
```



### python的有意思的特殊函数

1. `__init__(self, ...)`: 类的构造方法，用于初始化对象的状态。
2. `__str__(self)`: **返回对象的字符串表示形式，通常用于打印对象或调试目的**。
3. `__repr__(self)`: 返回对象的“官方”字符串表示形式，通常用于表示对象的“重现”。
4. `__eq__(self, other)`: **定义对象相等性的规则，通常与 `==` 运算符一起使用**。
5. `__ne__(self, other)`: 定义对象不相等性的规则，通常与 `!=` 运算符一起使用。
6. `__lt__(self, other)`: **定义对象之间小于关系的规则，通常与 `<` 运算符一起使用**。
7. `__le__(self, other)`: 定义对象之间小于等于关系的规则，通常与 `<=` 运算符一起使用。
8. `__gt__(self, other)`: 定义对象之间大于关系的规则，通常与 `>` 运算符一起使用。
9. `__ge__(self, other)`: 定义对象之间大于等于关系的规则，通常与 `>=` 运算符一起使用。
10. `__add__(self, other)`: 定义对象之间加法运算的规则，通常与 `+` 运算符一起使用。
11. `__sub__(self, other)`: 定义对象之间减法运算的规则，通常与 `-` 运算符一起使用。
12. `__mul__(self, other)`: 定义对象之间乘法运算的规则，通常与 `*` 运算符一起使用。
13. `__div__(self, other)`: 定义对象之间除法运算的规则，通常与 `/` 运算符一起使用。
14. `__len__(self)`: 返回对象的长度，**通常用于内置的 `len()` 函数**。
15. `__getitem__(self, key)`: **定义对象的索引访问行为，通常用于支持下标操作**。







### 快捷表达式ret

```
ret = ans[0] if len(ans) == 1 else -1
```


## 常用数据结构

```

```


### heap 堆 基于数组



heapq 就是 python 的 priority queue，`heapq[0]`即为堆顶元素。

heapq 的实现是小顶堆，如果需要一个大顶堆，常规的一个做法是把值取负存入，取出时再反转。
以下是借助 heapq 来实现 heapsort 的例子：

```text
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

```

**为什么可以用（key，item）实现自定义排序！！！！！！**

因为元组也可以直接比较大小，把一个元组当作一个数字其实就可以了。

**把key设置为元组的第一个，就可以实现自定义排序！！！！！！！**

```
>>> print((1,0) > (0,1)) 
True
```

**实际上，用对象的`__lt__` 方法，也是一样的原理，它是 Python 中用于定义对象之间小于关系的特殊方法**



### OrderedDict（双向哈希链表）

OrderedDict 能记录你 key 和 value 插入的顺序，底层其实是一个双向链表加哈希表的实现。我们甚至可以使用`move_to_end`这样的函数：

```text
>>> d = OrderedDict.fromkeys('abcde')
>>> d.move_to_end('b')
>>> ''.join(d.keys())
'acdeb'
# 放开头
>>> d.move_to_end('b', last=False)
>>> ''.join(d.keys())
'bacde'


ordered_dict = OrderedDict()
ordered_dict['a'] = 1
print(ordered_dict['a'])  # 输出 1
del ordered_dict['b']
for key, value in ordered_dict.items():
    print(key, value)

```



### 基于数组的deque（适用于双端插入删除）

`deque`中常见操作的时间复杂度：

1. 添加元素：
   - 在队列的右端添加元素（`append()`）：O(1) 时间复杂度，平均情况下是常数时间。
   - 在队列的左端添加元素（`appendleft()`）：O(1) 时间复杂度，平均情况下是常数时间。
2. 删除元素：
   - 从队列的右端删除元素（`pop()`）：O(1) 时间复杂度，平均情况下是常数时间。
   - 从队列的左端删除元素（`popleft()`）：O(1) 时间复杂度，平均情况下是常数时间。
3. 访问元素：
   - 访问队列中的任意位置的元素（按索引访问）：O(1) 时间复杂度。虽然`deque`是双链表实现的，但它是支持索引操作的，因为它内部实际上是用一个数组来存储元素，因此可以在常数时间内访问任意位置的元素

```
from collections import deque

# 创建一个空的 deque
my_deque = deque()
# 创建包含初始元素的 deque
my_deque = deque([1, 2, 3, 4, 5])
# 在右端添加一个元素
my_deque.append(6)

# 在左端添加一个元素
my_deque.appendleft(0)
# 从右端删除一个元素并返回
last_element = my_deque.pop()

# 从左端删除一个元素并返回
first_element = my_deque.popleft()

```





### 优先级队列 priorityQueue， 可以自定义key实现定制化

默认是先返回优先级最大的，可以修改__lt__实现不一样的顺序

```
import queue

# 定义一个包含优先级和数据的类
class MyItem:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
    
    # 定义 __lt__ 方法，用于比较对象的优先级
    def __lt__(self, other):
        return self.priority < other.priority

# 创建优先级队列
pq = queue.PriorityQueue()

# 向队列中添加元素
pq.put(MyItem(3, 'Apple'))
pq.put(MyItem(1, 'Banana'))
pq.put(MyItem(2, 'Orange'))

# 从队列中取出元素
while not pq.empty():
    item = pq.get()
    print(item.priority, item.value)

```

 
