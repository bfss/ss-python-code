class Human():
    """表示人类的类"""

    def __init__(self,name,age):
        """初始化方法（构造方法）"""
        self.name=name
        self.age=age

    def sleep(self):
        """睡觉"""
        print(self.name+"正在睡觉")

    def eat(self):
        """吃饭"""
        print(self.name+"正在吃饭")

bfss=Human('北方素素',30)

bfss.eat()