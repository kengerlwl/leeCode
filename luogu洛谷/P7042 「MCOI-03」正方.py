# #include<iostream>
# #include<algorithm>
# #include<cstdio>
# #define int long long
# using namespace std;
# int q;
# int len[5];
# signed main(){
# 	scanf("%lld",&q);
# 	for(int i=1;i<=q;++i){
# 		scanf("%lld%lld%lld%lld",&len[1],&len[2],&len[3],&len[4]);
# 		sort(len+1,len+4+1);
# 		if(len[1]+len[4]!=len[2]+len[3]){
# 			cout<<0<<endl;
# 			continue;
# 		}
# 		if(len[1]==len[2]&&len[2]==len[3]&&len[3]==len[4]){
# 		cout<<1<<endl;
# 		}else{
# 			if(len[1]==len[2]&&len[3]==len[4]){
# 				cout<<4<<endl;
# 			}else{
# 				if(len[1]==len[2]||len[3]==len[4]){
# 					cout<<2<<endl;
# 				}else{
# 					if(len[1]+len[4]==len[2]+len[3]){
# 						cout<<8<<endl;
# 					}else{
# 						cout<<0<<endl;
# 					}
# 				}
# 			}
# 		}
# 	}
# 	return 0;
# }
