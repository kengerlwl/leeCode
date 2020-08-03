class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]

        num2 = num2[::-1]

        l1= len(num1)
        l2 = len(num2)

        length = max(len(num1), len(num2))
        ans = [0] * (length+1)
        tmp = 0  # 进位
        for i in range(length):



            n1=0
            n2=0
            if i < l1:
                n1 = int(num1[i])
            if i < l2:
                n2 = int(num2[i])


            ans[i] = ((n1 + n2)  + tmp) % 10

            if  ((n1 + n2)  + tmp)//10 == 1:
                tmp = 1
            else:
                tmp =0
        ans[length] = tmp
        # print(ans)


        s1 = ""

        for i  in range(length):
            s1 += str(ans[i])
        if ans[length] ==1:
            s1 +="1"
        return s1[::-1]
        # print(s1)





ans  = Solution.addStrings(None, '99', '9')
print(ans)