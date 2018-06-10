names=['bf','ss','bfss','ssbf','bsfs']

print(names[:])

names1=names
names2=names[1:4]

print(names1)
names.append('ssbf')
print(names1)
print(names2)

print(type(names))
print(type(names[1:2]))

print(names2[1:2])


print(type(float(1)))
print(type(int(1.1)))
print(type("1"))

names3=('bf','ss')

for name in names3:
    print(name)

print(names3[1])


bf_grades=[1,2,3]
ss_grades=[4,5,6]
grades=[bf_grades,ss_grades]
print(grades)