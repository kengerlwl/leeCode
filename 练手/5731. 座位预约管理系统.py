import  heapq

class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.f = {}
        self.queue = []
        for i in  range(1 , n+1):
            self.f[i] = True
            heapq.heappush(self.queue, i)

    def reserve(self):
        """
        :rtype: int
        """
        a = heapq.heappop(self.queue)
        print(a)
        return a
        # for i in self.f:
        #     if self.f[i]:
        #         self.f[i] = False
        #         return i
        #
        # return -1


    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.queue, seatNumber)
        # self.f[seatNumber] = True



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)