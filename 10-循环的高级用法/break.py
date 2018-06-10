# break举例
count=1
message=""
while count<20:
    message=input('该输入啦')
    if message=='q':
        break
    count+=1

print(count)
for i in range(20):
    print(i)
    if i==4:
        break