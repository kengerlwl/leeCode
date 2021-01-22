解法二：动态规划 + 二分查找
解题思路：
降低复杂度切入点： 解法一中，遍历计算 dpdp 列表需 O(N)O(N)，计算每个 dp[k]dp[k] 需 O(N)O(N)。

动态规划中，通过线性遍历来计算 dpdp 的复杂度无法降低；
每轮计算中，需要通过线性遍历 [0,k)[0,k) 区间元素来得到 dp[k]dp[k] 。我们考虑：是否可以通过重新设计状态定义，使整个 dpdp 为一个排序列表；这样在计算每个 dp[k]dp[k] 时，就可以通过二分法遍历 [0,k)[0,k) 区间元素，将此部分复杂度由 O(N)O(N) 降至 O(logN)O(logN)。
设计思路：

新的状态定义：
我们考虑维护一个列表 tailstails，其中每个元素 tails[k]tails[k] 的值代表 长度为 k+1k+1 的子序列尾部元素的值。
如 [1,4,6][1,4,6] 序列，长度为 1,2,31,2,3 的子序列尾部元素值分别为 tails = [1,4,6]tails=[1,4,6]。
状态转移设计：
设常量数字 NN，和随机数字 xx，我们可以容易推出：当 NN 越小时，N<xN<x 的几率越大。例如： N=0N=0 肯定比 N=1000N=1000 更可能满足 N<xN<x。
在遍历计算每个 tails[k]tails[k]，不断更新长度为 [1,k][1,k] 的子序列尾部元素值，始终保持每个尾部元素值最小 （例如 [1,5,3]][1,5,3]]， 遍历到元素 55 时，长度为 22 的子序列尾部元素值为 55；当遍历到元素 33 时，尾部元素值应更新至 33，因为 33 遇到比它大的数字的几率更大）。
tailstails 列表一定是严格递增的： 即当尽可能使每个子序列尾部元素值最小的前提下，子序列越长，其序列尾部元素值一定更大。
反证法证明： 当 k < ik<i，若 tails[k] >= tails[i]tails[k]>=tails[i]，代表较短子序列的尾部元素的值 >> 较长子序列的尾部元素的值。这是不可能的，因为从长度为 ii 的子序列尾部倒序删除 i-1i−1 个元素，剩下的为长度为 kk 的子序列，设此序列尾部元素值为 vv，则一定有 v<tails[i]v<tails[i] （即长度为 kk 的子序列尾部元素值一定更小）， 这和 tails[k]>=tails[i]tails[k]>=tails[i] 矛盾。
既然严格递增，每轮计算 tails[k]tails[k] 时就可以使用二分法查找需要更新的尾部元素值的对应索引 ii。
算法流程：

状态定义：

tails[k]tails[k] 的值代表 长度为 k+1k+1 子序列 的尾部元素值。
转移方程： 设 resres 为 tailstails 当前长度，代表直到当前的最长上升子序列长度。设 j∈[0,res)j∈[0,res)，考虑每轮遍历 nums[k]nums[k] 时，通过二分法遍历 [0,res)[0,res) 列表区间，找出 nums[k]nums[k] 的大小分界点，会出现两种情况：

区间中存在 tails[i] > nums[k]tails[i]>nums[k] ： 将第一个满足 tails[i] > nums[k]tails[i]>nums[k] 执行 tails[i] = nums[k]tails[i]=nums[k] ；因为更小的 nums[k]nums[k] 后更可能接一个比它大的数字（前面分析过）。
区间中不存在 tails[i] > nums[k]tails[i]>nums[k] ： 意味着 nums[k]nums[k] 可以接在前面所有长度的子序列之后，因此肯定是接到最长的后面（长度为 resres ），新子序列长度为 res + 1res+1。
初始状态：

令 tailstails 列表所有值 =0=0。
返回值：

返回 resres ，即最长上升子子序列长度。
复杂度分析：

作者：jyd
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

