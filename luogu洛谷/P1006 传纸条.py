# #include <stdio.h>
# #include <algorithm>
# #include <string.h>
# using namespace std;
# int num[60][60];
# int dp[60][60][60][60];
# int main()
# {
#     int m,n;
#     while(scanf("%d%d",&m,&n)!=EOF)
#     {
#         memset(dp,0,sizeof(dp));
#         for(int i=1;i<=m;i++)
#             for(int j=1;j<=n;j++)
#             scanf("%d",&num[i][j]);//输入矩阵
#         for(int i=1;i<=m;i++)
#             for(int j=1;j<=n;j++)
#                 for(int k=1;k<=m;k++)
#                     for(int l=j+1;l<=n;l++)//让l从j+1开始
#                     {
#                         dp[i][j][k][l]=max(max(dp[i-1][j][k-1][l],dp[i][j-1][k][l-1]),max(dp[i-1][j][k][l-1],dp[i][j-1][k-1][l]))+num[i][j]+num[k][l];
#                     }//由于坐标不会重复，无需再特判
#         printf("%d\n",dp[m][n-1][m-1][n]);//需要注意此时输出的答案是在哪里的值
#         //因为终点和起点储存的值都是0，所以才能这样，否则还需要加上一次终点的值
#     }
#     return 0;
# }