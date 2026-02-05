# Dunder method / Magic method / specific method

class Demo:
    def __init__(self,A):
        self.No = A 

    def __add__(self,other):   #self is compulsary instead of other you can write anything
        return self.No + other.No
    
    def __sub__(self,other):   #self is compulsary instead of other you can write anything
        return self.No - other.No
    
    def __mul__(self,other):   #self is compulsary instead of other you can write anything
        return self.No * other.No
    
    def __truediv__(self,other):   #self is compulsary instead of other you can write anything
        return self.No / other.No


obj1 = Demo(11)
obj2 = Demo(21)

print(11+21)        #32
print(obj1+obj2)    # __add__(obj1,obj2) #32
print(obj1-obj2) 
print(obj1*obj2) 
print(obj1/obj2) 
















