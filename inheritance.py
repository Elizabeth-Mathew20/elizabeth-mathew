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



