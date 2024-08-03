a=["anu","alen","akhil","ammu","appu"]
print(a)
print(type(a))
print(len(a))
print(a[3])
print(a[1:4])
print(a[0:])
print(a[-4:-1])
print("1" in a )
print("1" not in a )

a[3]="sonu"
print(a)

a.append("meenu")
print(a)

a.insert(2,"manu")
print(a)

b=[1,2,3,4,5,6,7,8]
print(b)

a.extend(b)
print(a)
b.extend(a)
print(b)

a=["anu","alen","akhil","ammu","appu"]
print(a)

a.remove("anu")
print(a)

a.pop(3)
print(a)

b=[1,2,3,4,5,6,7,8]
print(b)
b.pop(5)
print(b)

del b[3]
print(b)

a.clear()
b.clear()
print(a,b)

a.sort()
print(a)

a=["anu","alen","akhil","ammu","appu","manu","sona","meenu","nelson","sona"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)


a=["anu","alen","akhil","ammu","appu"]
print(a)
b=[1,2,3,4,5,6,7,8]
print(b)

x=a.copy()
print(x)

print(a+b)
for i in a:
    print(i)
for i in b:
    print(i)

