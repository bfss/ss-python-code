# 函数定义
def greet():
    """输出特定信息"""
    print("调用了我")

# 函数调用
greet()

# 传递一些参数
def greet2(message):
    """输出传递的参数"""
    print(message)

# 调用带参数的函数
greet2("我是参数")

# 通过位置传递实参
def greet3(name,message):
    """向特定的名字发送特定信息"""
    print(name+message)

greet3("bfss","你好")

# 通过形参传递实参
greet3(message="你好哇",name="bfss")

# 带默认参数的函数
def greet4(name,message="她挺好的"):
    """带默认参数的函数"""
    print(name+message)

# 当没有传递带默认参数的实参时，使用默认参数
greet4("bfss")