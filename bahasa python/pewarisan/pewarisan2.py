from math import pi

class shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass
    
    def fact(self):
        return "I am batman"
    
    def __init__(self):
        return self.name
    
class square(shape):
    def __init__(self,length):
        super().__init__("square")
        self.length = length
    
    