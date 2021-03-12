import pickle




#设置递归深度，为了解决数据存储问题
import sys
sys.setrecursionlimit(10000)




def loadData(filePath):
    output = open(filePath, 'rb')
    data=pickle.load(output)
    output.close()
    return data

def saveData(data, filePath):
    output = open(filePath, 'wb')
    pickle.dump(data, output)
    output.close()



if __name__=="__main__":
    a = [1,3,4,5,6]
    saveData(a, 'test.pkl')



