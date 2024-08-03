# a=open("file1.txt","x")

# a=open("file1.txt","w")
# a.write("india is my country")
# a=open("file1.txt","r")
# print(a.read())



# a=open("file2.txt","x")
# a=open("file1.txt","r")
# c=a.read()
# s=open("file2.txt","w")
# s.write(c)











a=open("samplefile.txt","x")
a=open("samplefile.txt","w")
a.write("my name is anu")
c=open("samplefile.txt","r")
print(c.read())



a=open("samplefile2.txt","x")
a=open("samplefile2.txt","w")
a.write("i am come from kochi")
c=open("samplefile2.txt","r")
print(c.read())


a=open("samplefile3.txt","x")
a=open("samplefile.txt","r")
a=open("samplefile2.txt","r")

c=a.read()
s=open("samplefile3.txt","w")
s.write(c)



a=open("samplefile2.txt","r")


c=a.read()
s=open("samplefile3.txt","a")
s.write(c)















