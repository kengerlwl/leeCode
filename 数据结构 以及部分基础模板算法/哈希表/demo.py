# https://python123.io/index/topics/data_structure/hash_table

class Hash:
    # 表的长度定位11
    def __init__(self):
        self.hash_table = [[None, None] for i in range(11)]

    # 散列函数
    def hash(self, k, i):
        h_value = (k + i) % 11
        if self.hash_table[h_value][0] == k:
            return h_value
        if self.hash_table[h_value][0] != None:
            i += 1
            h_value = self.hash(k, i)
        return h_value

    def put(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v

    def get(self, k):
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]


hash = Hash()
hash.put(1, 'wang')
print(hash.get(1))