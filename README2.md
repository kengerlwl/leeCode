# 概述
无论什么题目，首先都是理解题意。
从暴力解法出发，不断进行各种优化，最后大多自然而然，通过各种结论，技巧，归纳就能得到符合DP，DFS，剪枝等的解法。

写题很多时候要讲究思路技巧，不是说题目要你找什么就找什么，而是说你可以将找一个复杂的东西，转化为一个简单的东西，然后再进行计算。，例如lc416，可以转化为一个背包问题，然后再进行计算。

对于很多边界例如 index 是否-1. -2 等问题，直接举个例子测试处差值是多少既可

## 前缀和技巧

利用一个数组可以方便的计算出前n个的和
进阶的，可以利用前缀和数组，计算出任意区间的和，只需要计算两个前缀和的差值即可

## 贪心
贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。


## 直觉
就是利用对情况的分析，的出基于该应用场景的一些结论。
从而实现省略一些不必要的计算。
例如：134


## 双指针
- 双指针主要是利用两个指针，分别指向数组的不同位置，从而解决一些数组的问题。
- 或者指向同一个数组，但是不同的方向，从而解决一些问题。例如从两边向中间，或者从中间向两边。


## 滑动窗口
和双指针有些类似，但是滑动窗口主要是利用一个窗口，从而解决一些问题。
- 一般是利用一个窗口，从而解决一些问题。左右指针从左边一起向右边移动。或者从两边向中间移动。

**右边移动不了就移动左边，左边移动不了就移动右边**


## DFS和BFS
- 设置visited数组，记录是否访问过. 备忘录非常重要
- DFS容易爆栈，可以使用非递归的方法，使用栈来模拟递归

### BFS
适合于需要层级的题目。
通过广度优先搜索，我们可以找到最短路径。因为每次都是一层一层的搜索。那么距离一定是最短的。
- 相对来说更加消耗空间

### DFS
简单易实现：DFS 算法通常使用递归或栈来实现，代码相对较简单。
内存消耗较小：DFS 在搜索过程中只需要存储当前路径上的节点，所以内存消耗较小。


### 回溯
- 回溯算法是一种渐进式寻找并构建问题解决方式的策略。
相对于DFS来说，回溯算法更加的灵活，可以在DFS的基础上进行一些剪枝操作。**回溯是有比较强的路径概念的。**
- 回溯有一个模板，那就状态的回退。

```

void backtrack(路径, 选择列表)
{
    if (满足结束条件)
    {
        result.add(路径);
        return;
    }
    for (选择 : 选择列表)
    {
        做选择; // 也就是将选择加入路径
        backtrack(路径, 选择列表);
        撤销选择; // 也就是将选择从路径中删除
    }
}

```


## 二分
二分的思路不同于分治，分治是将问题分解成子问题，然后分别解决。
二分是每次排除一半的解，然后继续进行查找。
很多二分的变种问题，关键就是证明通过中间值，可以确定左或右边一定存在答案，

### 对结果进行二分
加入要求的是一个符合条件的值，那么可以对结果进行二分。最如，要求最大的满足要求的值，那么可以对结果进行二分。
这个要求结果具有单调性，也就是说，如果该值满足要求，比该值小的也满足。这就是一种单调性。（准确来说，这叫做二段性）


### 板子
注意好边界值的处理
```
public int binarySearch(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2; // 避免left和right很大的时候溢出

        if (nums[mid] == target) {
            return mid; // 找到目标值，返回索引
        } else if (nums[mid] < target) {
            left = mid + 1; // 目标在右边
        } else {
            right = mid - 1; // 目标在左边
        }
    }

    return -1; // 目标值不存在
}

```


```
public int binarySearchRecursive(int[] nums, int target) {
    return binarySearch(nums, target, 0, nums.length - 1);
}

private int binarySearch(int[] nums, int target, int left, int right) {
    if (left > right) {
        return -1; // 目标值不存在
    }

    int mid = left + (right - left) / 2;

    if (nums[mid] == target) {
        return mid; // 找到目标值，返回索引
    } else if (nums[mid] < target) {
        return binarySearch(nums, target, mid + 1, right); // 目标在右边
    } else {
        return binarySearch(nums, target, left, mid - 1); // 目标在左边
    }
}

```


# 数据结构

## 链表
- 快慢指针
- 双指针
- 给链表加一个默认的头结点，这样就不用考虑头结点的问题了。


# TOP150进度

- 数组 almost done
- 数学 done



# 一些小技巧


## 向上取整
除k向上取整
```
ans = (value -1) / k +1
```


## java 指定排序
```
            Integer[] nums2 = new Integer[n];
            for(int j = 0; j < n; j++){
                nums2[j] = in.nextInt();
            }
            Arrays.sort(nums2, new Comparator<Integer>(){
                public int compare(Integer a, Integer b){
                        return b-a;
                }
        });
```






## 溢出问题
解决java定义long类型却内存溢出的问题
原因是：a和b都是int类型，所以a*b计算的时候会默认将结果转换为int，即使最后赋值给long，此时计算结果已经是错误的了。

解决方案：把a*b计算表达式中任意一个变量转换为long类型。
```
int a = 1000000000;
int b = 20;
long c = a * b;
long d = (long)a * b;
long e = a * (long)b;
System.out.println("a=" + a);
System.out.println("b=" + b);
System.out.println("c=" + c);
System.out.println("d=" + d);
System.out.println("e=" + e);
```