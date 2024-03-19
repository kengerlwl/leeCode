// 二维动态数组，dp[i][j] 前i个数，和为k且满足要求的组合数量
// dp[i][j] 的转移方程为，求第i行时，
// 第i个数字的所有可能取值（不等于原数组）。然后将其所有可能性，分别计算出来与前面的加上。也就是说，其不是线性的先求j，再求j+1再依次。而是根据第i个数值的选择，依次计算
// #include <bits/stdc++.h>
// using namespace std;
// int main() {
// int n;
// cin >>n;
// vector<int> a(n);
// int sum = 0;

// int mod = 1e9 + 7;
// for(int i = 0; i < n; i++){
// cin >> a[i];
// sum += a[i];
// }
// vector<vector<long>> dp(n+1, vector<long>(sum + 1));
// dp[0][0] = 1;
// for(int i= 1; i <= n; i++) {
// for(int j = 1; j<= sum; j++) {
// for(int k = 1; k <= j-i +1; k++){
// if(a[i - 1] == k) continue;
// dp[i][j] = (dp[i][j] + dp[i -1][j -k]) % mod;
// }
// }
// }

// cout<<dp[n][sum]<<endl;

// 作者：牛客438958669号
// 链接：https://www.nowcoder.com/exam/test/78419136/submission?pid=52007812
// 来源：牛客网