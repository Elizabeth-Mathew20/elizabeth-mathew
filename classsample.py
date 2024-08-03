# class d:
#     x=10
# obj=d()
# print(obj.x)



# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# obj=person("sona",20)      
# print(obj.name)  
# print(obj.age)  





# class animal:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
# obj=animal("dog","black")
# print(obj.name, "is an animal")        
# print(obj.color, "animal")



class teach:
    pass




# function polymorphism

# a=("welcome to world")
# b="india is my country"
# c=["blue","black","pink",1,2,3]
# d={"name":"arun","age":20,"sub":"maths","place":"alappuzha"}
# e={1,2,3,4,5}

# d={1,2,3,4,5}
# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))
# print(len(e))






# inheritance

class vechile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def movement(self):
            print("move")

class car(vechile):
    pass
class plane(vechile):
    def movement(self):
        print("fly")
class boat(vechile):
    def movement(self):
        print("sailing")

obj=plane("emerates",45645)
obj1=car("swift",2345)  
obj2=boat("ship",45678909)  
for i in(obj,obj1,obj2):
    print(i.brand,i.model)
    i.movement()



