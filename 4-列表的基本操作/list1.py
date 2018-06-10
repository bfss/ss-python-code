color=['red','green','blue']
print(color)

print(color[1])
print(color[-2])

color[1]='pink'
print(color)

color.append('black')
print(color)

color.insert(1,'white')
print(color)

del color[0]
print(color)

color.pop()
print(color)

color.pop(0)
print(color)

popped_color=color.pop()
print(popped_color)

color=['red','green','blue','grey','blue']

color.remove('blue')
print(color)

color.sort()
print(color)

color.sort(reverse=True)
print(color)

color=['red','green','blue','grey','blue']

print(sorted(color,reverse=True))
print(color)

color=['red','green','blue','grey','blue']
color.reverse()
print(color)

print(len(color))

color=['red','green','blue','grey','blue']
# print(color[5])

people=[]
print(people[0])