def num():
    print("number")
num()   





def num(a,b):
    print(a-b)
num(50,10)    




def num(*a):
    print(a[4])
num(1,2,3,4,5,6,7,8,9,1,2,3,)    





def num(a,b,c,d):
    print(b)
num(a=6,b=54,c=8,d=0)    






def num(**z):
    print(z['t'])
num(a=1,b=5,o=4,r=9,w=2,t=2)


def num(color="black"):
    print(color)
num()    



s=["blue","white","pink"]
def num(a):
    for i in s:
        print(i)
num(s)



def num(x):
    return 5+x
print(num(3))



a=lambda s:s+4
print(a(5))



a=lambda p,s:p+s
print(a(20,10))



s=["one","two","three","four"]
z=list(map(lambda a:str.upper(a),s))
print(z)




a=[10,20,30,40,50,60,70,80,90,100,200,300,400,500]
z=list(filter(lambda p:p<50,a))
print(z)




a=[10,20,30,40,50,60,70,80,90,100,200,300,400,500]
z=list(filter(lambda p:p>50,a))
print(z)




a=lambda c:c+2
print(a(2))


















