class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        data = arr
        a = sorted(data);
        l = 0.05 * len(a)
        l = int(l)

        total =0
        count =0
        for i in range(l, len(a) - l):
            total += a[i]
            count +=1


        ans = total / count
        ans = float('%.5f' % ans)

        print(ans)
        return ans

class Solution(object):
    def trimMean(self, A):
        n = len(A)
        return sum(sorted(A)[n/20:n-n/20]) / float(n/10*9)

Solution.trimMean(None,[6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4])