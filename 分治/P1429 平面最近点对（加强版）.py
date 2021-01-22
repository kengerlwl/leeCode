
import math
class point():
    def __init__(self):
        self.x= None
        self.y=None


def calDis(a, b):
    tmp =  (a.x-b.x)**2 + (a.y-b.y)**2
    return tmp

#有点他妈的难


# #include<cstdio>
# #include<cstring>
# #include<algorithm>
# #include<cmath>
# using namespace std;
# const int N=2e5+10;
# int n,p[N],c[N];
# double x[N],y[N];
# bool cmp(int a,int b)
# {return (x[a]==x[b])?(y[a]<y[b]):(x[a]<x[b]);}
# bool cMp(int a,int b)
# {return y[a]<y[b];}
# double get_dis(int a,int b)
# {return sqrt((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]));}
# double Solve(int l,int r){
# 	double d=1e18;
# 	if(l==r)return d;
# 	if(l+1==r)return get_dis(p[l],p[r]);
# 	int mid=(l+r)>>1;
# 	double d1=Solve(l,mid);
# 	double d2=Solve(mid+1,r);
# 	d=min(d1,d2);
# 	int tot=0;
# 	for(int i=l;i<=r;i++)
# 		if(fabs(x[p[i]]-x[p[mid]])<=d)
# 			c[++tot]=p[i];
# 	sort(c+1,c+1+tot,cMp);
# 	for(int i=0;i<tot;i++){
# 		for(int j=i+1;j<=tot;j++){
# 			if(y[c[j]]-y[c[i]]>=d)break;
# 			double D=get_dis(c[i],c[j]);
# 			d=min(d,D);
# 		}
# 	}
# 	return d;
# }
# int main()
# {
# 	scanf("%d",&n);
# 	for(int i=1;i<=n;i++){
# 		scanf("%lf%lf",&x[i],&y[i]);
# 		p[i]=i;
# 	}
# 	sort(p+1,p+1+n,cmp);
# 	printf("%.4lf",Solve(1,n));
# }
