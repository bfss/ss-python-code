class Human():
    """一个人类的类"""
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def grow(self,age):
        """长了几岁"""
        if age<0:
            print("输入错误")
        else:
            self.age+=age
    
    def print_info(self):
        """输出信息"""
        print(self.name+"现在"+str(self.age)+"岁了")

b=Human("b",12)
b.print_info()
# 直接修改属性
b.age=-12
b.print_info()
# 通过方法修改
b.grow(-1)
b.print_info()
b.grow(1)
b.print_info()

class Yellow_Human(Human):
    """黄种人"""
    def __init__(self,name,age,skin):
        super().__init__(name,age)
        self.skin=skin

    def skin_color(self):
        """输出皮肤颜色"""
        print(self.skin)

    def print_info(self):
        """输出信息"""
        print(self.name+"现在"+str(self.age)+"岁了,他的皮肤颜色是"+self.skin)

# 子类对象
f=Yellow_Human("f",12,"黄色")
# 子类调用继承来的父类方法
f.grow(1)
# 子类调用重写的方法
f.print_info()