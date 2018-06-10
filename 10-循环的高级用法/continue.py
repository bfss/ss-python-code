# continue举例
current=-1
while current<20:
    current+=1
    if current%2!=0:
        continue
    
    print(current)

for i in range(20):
    if i ==4 or i==5 or i==6 or i==18:
        continue
    print(i)