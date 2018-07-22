# 逐行读取
with open('file.txt') as file_object:
    for line in file_object:
        print(line)

# 将文件的每一行存入列表
with open("file.txt") as file_object:
    lines = file_object.readlines()

print(type(lines))

for line in lines:
    print(line)