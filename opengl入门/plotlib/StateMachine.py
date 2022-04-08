# 这个是用来保存函数执行的，每次都可以存入函数和参数，并且在pop执行。




# 饿汉单例模式 通过keyword映射
class StateKw(object):
    __instane = None
    def __int__(self):
        self.stack = []

    # 通过覆盖__new__方法来控制对象的创建。
    def __new__(cls, *args, **kwargs):
        # hasattr用于查看对象cls是否有instance属性，该属性作用是检测该类是否已经生成了一个对象
        if cls.__instane == None:
            cls.__instane = object.__new__(cls)
            return cls.__instane
        else:
            return cls.__instane


    def pushState(self,fun, **kwargs):
        """
        状态机push
        fun是需要执行的函数
        kwargs是执行参数
        """
        self.stack.append([fun,kwargs])
        pass


    def popState(self):
        fun,kwargs = self.stack[len(self.stack)-1]
        self.stack.__delitem__(len(self.stack)-1)
        print(kwargs)
        fun(**kwargs)


# 饿汉单例模式 通过arg参数数组形式
class StateArg(object):
    __instane = None
    stack = []
    def __int__(self):
        pass

    # 通过覆盖__new__方法来控制对象的创建。
    def __new__(cls, *args, **kwargs):
        # hasattr用于查看对象cls是否有instance属性，该属性作用是检测该类是否已经生成了一个对象
        if cls.__instane == None:
            cls.__instane = object.__new__(cls)
            return cls.__instane
        else:
            return cls.__instane


    def pushState(self,fun, *args):
        """
        状态机push
        fun是需要执行的函数
        kwargs是执行参数
        """
        self.stack.append([fun,args])
        pass


    def popState(self):
        fun,args = self.stack[len(self.stack)-1]
        self.stack.__delitem__(len(self.stack)-1)
        # print(args)
        fun(*args)



def print1(a, b):
    print("a",a)
    print("b", b)


if __name__ == '__main__':


    # sta = StateKw()
    # sta.__int__()
    # di= {"a":1, "b":2}
    # sta.pushState(print1,**di)
    #
    # sta.popState()
    #

    sta = StateArg()
    sta.__int__()
    l = [1,2]
    sta.pushState(print1, *l)
    sta.popState()
