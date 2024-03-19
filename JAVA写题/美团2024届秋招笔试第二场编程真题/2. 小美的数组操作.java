// 大体上分两种情况
// （1）数组的和（sum），能够整除数组元素的个数（n）。这时，众数就是数组的平均数avg，众数的数量是n。此时计算操作数，那就是每个元素到平均数avg的距离之和除以2，除以二是因为，每一次操作，一个数加一，另一个数减一。因此，计算每个元素到平均数avg的距离之和，相当于把每一次操作算了两遍，后面除以2才是真正的操作数
// （2）数组的和（sum），不能整除数组元素的个数（n）。这时，众数的数量是n-1，把数组中的一个数当做垃圾桶（称之为垃圾数），可以把多余的操作都用在垃圾数上，从而让另外n-1个数相同，达到n-1个众数。运用贪心的思想，这个垃圾数一定是数组的最大值或者最小值。

// 我们以最大值作为垃圾数为例，此时，众数就是剩下n-1个数的平均值（avg），但是有可能不能整除，所以，众数有可能是avg，也有可能是avg+1，（C++默认向下取正）。所以分众数分别是avg和avg+1两种情况讨论，假定众数就是avg，我们现在去计算操作数，定义了两个变量a，b，a用来统计减操作的次数，b用来统计加操作的次数，整体的操作数是max(a,b)，a和b的差值就是用在垃圾数上的操作次数。同理，定义c，d去计算众数是avg+1情况下的操作数。最终取min(max(a,b),max(c,d))为最终的操作数。所以，comp函数可以计算数组l到r元素的操作数。

// 同理，最小值作为垃圾数的操作数也通过comp函数计算。最终的结果就是最大值作为垃圾数，和最小值作为垃圾数两种情况下的操作数的最小值
// #include <bits/stdc++.h>
// using namespace std;

// int main() {
// int n;
// cin >> n;
// vector<long long> nums(n);
// for (int i=0; i<n; ++i) {
// cin >> nums[i];
// }
// long long sum = accumulate(nums.begin(), nums.end(), (long long)0);
// if (sum%n==0) {
// long long avg = sum/n;
// long long ans = 0;
// for (auto a:nums) {
// ans += abs(a-avg);
// }
// cout << ans/2 << endl;
// return 0;
// }
// sort(nums.begin(), nums.end());
// function<long long(vector<long long>&, int, int)> comp = [&](vector<long
// long>& nums, int l, int r) {
// long long tot = 0;
// for (int i=l; i<=r; ++i) {
// tot += nums[i];
// }
// long long avg = tot/(r-l+1);
// long long avg2 = avg+1;
// long long a = 0;
// long long b = 0;
// long long c = 0;
// long long d = 0;
// for (int i=l; i<=r; ++i) {
// if (nums[i]>=avg) a+=nums[i]-avg;
// else b+=avg-nums[i];
// if (nums[i]>=avg2) c+=nums[i]-avg2;
// else d+=avg2-nums[i];
// }
// return min(max(a, b), max(c, d));
// };
// long long res1 = comp(nums, 0, n-2);
// long long res2 = comp(nums, 1, n-1);
// cout << min(res1, res2) << endl;
// return 0;
// }