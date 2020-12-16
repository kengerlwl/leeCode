# https://www.luogu.com.cn/problem/P1404


# 方法1
#
# 求一个子段，它的和最大，没有“长度不小于L”这个限制。这个可以用动态规划解决。 **** d[i]=max(d[i-1]+A[i],0.0);**** d[i]为以i结尾的最大子段和
#
# 如何将“限制性”转化为一般情况：
#
# 设s[i]为以i结尾且长度不小于L的最大子段和，A[i]为原数组，sum[i]为前缀和。因为长度要不小于L,所以从A[i-L]一直到A[i]是必选的，总和为sum[i]-sum[i-L]。 前面i-L个数可选可不选，要想和最大，就要加上以a[i-L]结尾的最大子段和，所以s[i]=sum[i]-sum[i-L]+d[i-L] (前面i-L个数的最大子段和)。最后在s[i]中取一个最大值就是ans。也可以不用s数组，直接在过程中取最大值
#


#  之所以要减去平均值， 是因为要求的是平均值，为了将总和最大与平均值联系起来。 NB


# #include<iostream>
# #include<cstdio>
# #include<cstring>
# using namespace std;
#
# const double eps=1e-7;
# const int maxn=1e5+10;
# double a[maxn],sum[maxn],d[maxn],l,r,b[maxn];
# int n,L;
#
# void init()
# {
# 	scanf("%d%d",&n,&L);
# 	for(int i=1;i<=n;i++){
# 		scanf("%lf",&a[i]);
# 		r=max(r,a[i]);
# 	}
# }
#
#
# double Largest_subsum()
# {
# /*	int min_val=0,ans=-maxn;
# 	for(int i=L;i<=n;i++){
# 		min_val=min(min_val,sum[i-L]);
# 		ans=max(ans,sum[i]-min_val);
# 	}*/
#     double ans=0;
# 	for(int i=1;i<=n;i++)
# 	  d[i]=max(d[i-1]+b[i],0.0);
# 	for(int i=L;i<=n;i++){
# 		ans=max(ans,sum[i]-sum[i-L]+d[i-L]);
# 	}
# 	return ans;
# }
#
#
# bool check(double x)
# {
# 	for(int i=1;i<=n;i++)  b[i]=a[i]-x;
# 	for(int i=1;i<=n;i++){
# 		sum[i]=sum[i-1]+b[i];
# 	}
# 	double ans=Largest_subsum();
# 	if(ans>0)  return true;
# 	else  return false;
# }
#
# void Binary_search()
# {
# 	while(r-l>eps){
# 		double mid=(r+l)/2;
# 		if(check(mid))
# 		  l=mid;
# 		else
# 		  r=mid;
# 	}
# 	printf("%d",int(r*1000));
# }
#
# int main()
# {
# 	init();
# 	Binary_search();
# 	return 0;
# }