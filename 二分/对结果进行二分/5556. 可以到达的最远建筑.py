class Solution:
    def furthestBuilding(self, h: List[int], b: int, d: int) -> int:
        n=len(h)
        a=[]
        for i in range(1,n):
            a.append(h[i]-h[i-1])
        def check(mid):#验证能否到达位置mid
            v=sorted(i for i in a[:mid] if i>0)
            ans=0
            i=0
            t=b
            while i<len(v) and t>=v[i]:
                t-=v[i]
                i+=1
            return i+d>=len(v)


        # 二分判断
        left,right=0,n-1
        while left<right:
            mid=(left+right+1)//2
            if check(mid):
                left=mid
            else:
                right=mid-1
        return left



Solution.furthestBuilding(None, heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1)