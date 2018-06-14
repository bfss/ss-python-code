def greet_every(names):
    """问候列表中的每一个名字"""
    for name in names:
        print("你好啊~"+name)

names=['北方素素','卫宫士郎','言峰绮礼']
greet_every(names)

# 对列表进行一下修改
def update(name,names):
    """向列表中添加一个元素"""
    names.append(name)
    print(names)

update('呆毛王',names)
print(names)

# 传递列表的副本
update('阿尔托莉雅',names[:])
print(names)

# 接受任意数量的参数的函数
def fate(*names):
    """输出参数"""
    for name in names:
        print(name)
    # 输出参数的类型
    print(type(names))

# 传递一个参数
fate("阿尔托莉雅")
# 两个参数
fate("阿尔托莉雅","美狄亚")

# 一个可以传入任意数量关键字参数的函数
def fate2(**ms):
    """输出参数"""
    for m,s in ms.items():
        print("Servant:"+m+"的Master是："+s)
    print(type(ms))

# 传递一个参数
fate2(saber='卫宫士郎')

# 传递两个参数
fate2(saber='卫宫士郎',caster='葛木宗一郎')

# 包含返回值的函数
def add(a,b):
    """求两个数之和，并把结果返回"""
    return a+b
# 把返回值存储到c中
c=add(1,3)
print(c)