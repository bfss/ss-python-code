id={'321':'bf','123':'ss','332':'bf'}

print(id['123'])

id['233']='ssbf'

print(id)

id['123']='bbfff'

print(id)

del id['233']
print(id)

for key,value in id.items():
    print(key)
    print(value)

print("\n")


for key in id.keys():
    print(key)
print("\n")
for key in id:
    print(key)

print(type(id.keys()))

for key in sorted(id.keys()):
    print(key)

print("\n")

for value in id.values():
    print(value)

print()
for value in set(id.values()):
    print(value)

id1={'id':'123','name':'bf'}
id2={'id':'321','name':'ss'}

ids=[id1,id2]

print(ids)

favorite_fruit={
         'bfss':['apple','banana'],
         'ssbf':['orange','apple'],
}

usernames={
       'bfss':{
                 'name':'ss',
                 'tel':'2222',
        },
       'ssbf':{
                 'name':'bf',
                 'tel':'1111',
        },
}
