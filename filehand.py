import os
# a=open("file hand.txt","r")

# print(a.read())
# print(a.read(4))
# print(a.readline())
# print(a.readline())
# print(a.readline())


# a=open("file hand.txt","a")
# (a.write("are you happy"))
# a.close()

# a=open("file hand.txt","r")
# print(a.read())



a=open("file hand.txt","w")
a.write("india is my country")
a.close()
a=open("file hand.txt","r")
print(a.read())



# a=open("new file.txt","x")
# os.remove("new file.txt")



os.rmdir("sample")
