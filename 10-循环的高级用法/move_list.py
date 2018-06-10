old_list=['green','blue','yellow']
new_list=[]

while old_list:
    new_list.append(old_list.pop())

print(old_list)
print(new_list)