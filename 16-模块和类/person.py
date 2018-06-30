"""人的模块"""
from degree import Degree

class Person():
    """一个人的类"""
    def __init__(self,name,age,deg,school):
        self.name=name
        self.age=age
        self.degree=Degree(deg,school)

    def print_info(self):
        """输出信息"""
        print(self.name+"现在"+str(self.age)+"岁,他毕业于"+self.degree.school+",学位是"+self
        .degree.deg)





