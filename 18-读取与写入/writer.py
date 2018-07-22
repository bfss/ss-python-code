# 写入文件
with open("file2.txt","w") as file_object:
    file_object.write("我是被北方素素写入的\n")
    file_object.write("我是第二行被写入的\n")

# 附加
with open("file2.txt","a") as file_object:
    file_object.write("我是被追加到末尾的")