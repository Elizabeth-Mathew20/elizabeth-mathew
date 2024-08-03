a={1,2,3,4,5}
print(a)
print(type(a))
print(len(a))

a.add(6)
print(a)

b={10,11,12,13}
b.update(a)
print(b)

b.remove(11)
print(b)

b.discard(12)
print(b)

b.discard(22)
print(b)

s={"alappuzha","kannur","kerala","malapuram"}
p={"ernakulam","iduki","kottayam","kerala"}
print(s)
print(p)

z=s.union(p)
print(z)

z=s.difference(p)
print(z)

z=s.intersection(p)
print(z)

v=p.copy()
print(v)
