file_name = input("输入要读取的文件名:")

try:
    with open(file_name) as f:
        text = f.read()
except FileNotFoundError:
    #print("啊呀，文件不存在")
    pass
else:
    print(text)


print("文件读取完毕")