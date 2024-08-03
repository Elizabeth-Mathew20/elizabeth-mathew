s=(1,2,3,4)
print(s)
print(type(s))
print(len(s))

print([3])
print(s[1:])
print(s[1:2])

for i in s:
    print(i)

p=("black")
print(p)
print(type(p))    

x=list(s)
print(x)

x.append(5)
print(x)

x.insert(2,10)
print(x)
s=tuple(x)
print(s)

c=s*2
print(c)

c=p*2
print(c)