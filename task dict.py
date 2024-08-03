
s={"name":"anu","roll no":10,"sub":"english","mark":40}
print(s)
print(type(s))
print(len(s))
print(s["roll no"])

print(s.get("name"))
print(s.keys())
print(s.items())
print(s.values())

s["roll no"]=25
print(s)

s.update({"name":"manu"})
print(s)

s.pop("sub")
print(s)

s.popitem()
print(s)

del s["roll no"]
print(s)


s.clear()
print(s)