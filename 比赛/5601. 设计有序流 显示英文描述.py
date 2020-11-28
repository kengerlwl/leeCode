class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.num ={}
        self.ptr =1


    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        self.num[id] = value

        if id == self.ptr:
            index = sorted(self.num)
            ans = []
            flag =True
            ans.append(value)
            self.ptr= id+1
            for i in range(len(index)):
                if index[i] > id:
                    if index[i] - index[i-1] != 1:

                        break

                    ans.append(self.num[index[i]])
                    # print(index[i])
                    self.ptr =  index[i]+1


            # print(self.ptr)
            return ans
        else:
            return []

if __name__ == '__main__':
    o = OrderedStream(5)
    print(o.insert(3,'1'))
    print(o.insert(1, 'a'))
    print(o.insert(2, '1'))
    print(o.ptr)
    print(o.insert(5,'e'))
    print(o.insert(4, 'a'))




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)