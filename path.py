import os

#当前文件目录路径
FileDir = os.path.abspath(os.path.dirname(__file__))

#读取某个目录中的所有文件名称
def getPathFile(path):
    ans = []
    for i,j,k in os.walk(path): #三个数据分别是当前路径，文件夹名称数组， 文件数组
        ans.append([i, k])
        #print(i,j,k) 
    return ans

if __name__=="__main__":

    print( '***获取当前目录***')
    print( os.getcwd())
    print( os.path.abspath(os.path.dirname(__file__)))

    print( '***获取上级目录***')
    print( os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print( os.path.abspath(os.path.dirname(os.getcwd())))
    print( os.path.abspath(os.path.join(os.getcwd(), "..")))

    print( '***获取上上级目录***')
    print( os.path.abspath(os.path.join(os.getcwd(), "../..")))

