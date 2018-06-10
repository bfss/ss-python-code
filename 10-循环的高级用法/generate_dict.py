# 获取用户输入-姓名和喜欢的水果，并存储进字典中
favorite={}
# 设置一个标识，用来判断时候还要继续循环
flag=True

while flag:
    name=input("你的名字？")
    fruit=input("你喜欢的水果？")

    favorite[name]=fruit

    repeat=input("还有要输入的吗？")
    if repeat=='no':
        flag=False

print('----------------------------------')
for name,fruit in favorite.items():
    print(name+'最喜欢的水果是'+fruit)