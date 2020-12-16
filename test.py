# a = 'Aaaaa'
# print(a.count('a'))  #统计某个字符串的次数
# print(a.lower())
# print(a.upper())
#
# b= a.replace('a', 'b')  # 进行替换
# print(b)


# x  = 10
# ans  = eval('x + 2')
# print(ans)
#
# ans = eval('pow(2,x)')
# print(ans)




# x = 1.512187
# print(round(x,4))  # 四舍五入保留几位
# print(round(x,100)) # 但是不能强制输出多位
#
#
# print('%.4f'%x)
# print('%.10f'%x)
#
# import math
# print(math.floor(x)) # 向下取整
# print(math.ceil(x))  #向上取整




# import re   #引入正则表达式包
# s  = "abcadffiwef/sdfsdf"
# b = re.match('abc.*', s)
# print(b[0])
#
# c= re.search('c.*', s)
# print(c[0])


# s = 'asdf{},adfsdf{}'
# print(s.format(2,1))
#
# print('asdf{0},adfsdf{2}'.format(1,2,3)) #利用下标进行索引
#
# print('asdf{name},adfsdf{pwd}'.format(name = 1, pwd = 32))  # 利用字符串进行替换，参数
#
# print('{:.2f}'.format(2.339))


# import math
#
# def factorial_(n):
#     result=1
#     for i in range(2,n+1):
#         result=result*i
#     return result
#
# def comb_1(n,m):
#     return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))  #直接使用math里的阶乘函数计算组合数
#
# def comb_2(n,m):
#     return factorial_(n)//(factorial_(n-m)*factorial_(m))              #使用自己的阶乘函数计算组合数
#
# def perm_1(n,m):
#     return math.factorial(n)//math.factorial(n-m)                        #直接使用math里的阶乘函数计算排列数
#
# def perm_2(n,m):
#     return math.factorial(n)//math.factorial(n-m)                        #使用自己的阶乘函数计算排列数
#
# if __name__=='__main__':
#     print(comb_1(3,2))
#     print(comb_2(3,2))
#     print(perm_1(3,2))
#     print(perm_2(3,2))



# #将10 进制转化为N进制
# def TentoN(num, N):
#     num = int(num)
#     ans =[]
#     while num !=0:
#         rest = num % N
#         num = num // N
#         ans.append(rest)
#
#     ans.reverse()
#     return ans
#
#
# # 将N进制转化为10进制
# def NtoTen(num, N):
#     ans =0
#     num = str(num)
#     for i in num:
#         ans= ans * N + int(i)
#
#     return ans
#
# print(NtoTen(10, 2))
#
# print(TentoN(10,8))


s = '123456'
print(s[0:1])