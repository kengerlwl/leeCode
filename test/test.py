temp = {'a':1}


def my_first(**args):
    print(args)


my_first(**temp)  # temp只算一个参数，除非你有这个需求

