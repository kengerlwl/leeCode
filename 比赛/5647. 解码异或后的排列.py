# 将N进制转化为10进制
def NtoTen(num, N):
    ans =0
    num = str(num)
    for i in num:
        ans= ans * N + int(i)

    return ans

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True

    def findMax(self, a):
        a  = '{:018b}'.format(a).replace('0b', '')
        tree = self.lookup
        ans = ''
        for i in a:
            if i == '0':
                if '1' in tree:
                    tree = tree['1']
                    ans += '1'
                else:
                    tree = tree['0']
                    ans += '0'
            else:
                if '0' in tree:
                    tree = tree['0']
                    ans +='1'
                else:
                    tree = tree['1']
                    ans+='0'

        return NtoTen(ans, 2)









class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        start =1
        now = start
        maxV = max(encoded)
        length = len(encoded) +1
        first = encoded[0]
        list = [first]
        trieT  =Trie()
        for i in range(1, len(encoded)):
            first = first^encoded[i]
            list.append(first)
        for i in list:
            s  = '{:018b}'.format(i).replace('0b','')
            # print(s)
            trieT.insert(s)




        for j in range(1, max(encoded)):
            # print('\n\n')
            now = j
            # print(now)
            ans = [now]
            flag= True
            # print(trieT.findMax(j))
            if trieT.findMax(j) > length:
                print(j)
                continue

            for i in range(len(encoded)):
                # print(encoded)
                tmp = encoded[i]
                # if j == 8:
                #     print(now, tmp)
                pre  = now
                now = now^tmp
                if now == 0 or now > length:
                    # print(j, ans)
                    flag =False
                    break
                ans.append(now)


                # print(now)
            if flag:
                # print(j,ans, flag)
                # pass
                break
        print(ans)
        return ans

Solution.decode(None,encoded =[12,6,11,10,5,3,4,6])