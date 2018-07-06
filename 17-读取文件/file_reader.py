with open('17.txt') as f:
    content = f.read()
    print(content.rstrip())

with open('..\\1.txt') as f:
    content = f.read()
    print(content.rstrip())

with open('txts\\2.txt') as f:
    content = f.read()
    print(content.rstrip())


with open('G:\\素素带你学\\python\\17-读取文件\\17.txt') as f:
    content = f.read()
    print(content.rstrip())


with open(r'G:\素素带你学\python\17-读取文件\17.txt') as f:
    content = f.read()
    print(content.rstrip())


print("\n")
# f = open('17.txt')
# content = f.read()
# print(content)
# f.close()