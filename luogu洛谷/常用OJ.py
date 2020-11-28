
import  numpy as np

#转化数据类型为int
def change(numList):
    ans =[]
    for i in numList:
        ans.append(int(i))
    return ans



#生成 维度
# a= getMatrix(3, 3)
#
# a =np.array(a)
# print(a.shape)
# (3, 3, 3)
def getMatrix(deep,length):
    if deep != 1:
        return [getMatrix(deep -1, length) for i in range(length)]
    else:
        return [0 for i in range(length)]

import copy


#正经得维度矩阵创建
# a = np.array(getMatrixNew([3, 4], 0))
# print(a)
# print(a.shape)
def getMatrixNew(List, value=0):
    print(List)
    if len(List) != 1:
        nowLength = List[0]

        new = copy.deepcopy(List[1:len(List)])

        return [getMatrixNew(new, value) for i in range(nowLength)]
    else:
        return [value for i in range(List[0])]



if __name__ == '__main__':
    a  = np.array(getMatrixNew([3,4],0))
    print(a)
    print(a.shape)



