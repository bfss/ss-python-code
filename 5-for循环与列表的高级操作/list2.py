names=['bf','ss','bfss']

for name in names:
    print(name)
    print("hello~\n")

print("It is a good day")

for value in range(2,11,2):
    print(value)

numbers=list(range(1,5))
print(numbers)

digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares=[]
for value in range(1,11):
    squares.append(value**2)

print(squares)

squares2=[value**2 for value in range(1,11)]
print(squares2)