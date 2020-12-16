n, k = input().split(' ')
n = int(n)
k = int(k)

s= input()


#用树来分析， 典型的中间存储的是子规模

def dfs(s, k):

    # 转化为更下规模的情况
    pass










# #include<cstdio>
# #include<cstring>
# #include<iostream>
# #include<algorithm>
# using namespace std;
# char x[45];
# int n,m,ans;
# long long dis[45][45],f[45][45];
# int main(){
#     scanf("%d%d",&n,&m);
#     for(int i=1;i<=n;i++){
#         cin>>x[i];
#         dis[i][i]=x[i]-'0';
#     }
#     for(int i=1;i<=n;i++)
#         for(int j=i+1;j<=n;j++)
#             dis[i][j]=dis[i][j-1]*10+x[j]-'0';
#     for(int i=1;i<=n;i++)    f[i][0]=dis[1][i];
#     for(int k=1;k<=m;k++)
#         for(int i=k+1;i<=n;i++)
#             for(int j=k;j<i;j++)
#                 f[i][k]=max(f[i][k],f[j][k-1]*dis[j+1][i]);
#     cout<<f[n][m];
# }