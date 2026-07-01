
## class to use Arithmatic operation in python

class MathOperation : 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Addition
    def add(self) :
        return self.x + self.y
    # Subtraction
    def sub(self) :
        return self.x - self.y
    # Multiplication 
    def mul(self) :
        return self.x  * self.y
    # Division  
    def div(self) :
        return self.x / self.y 
    
    def __str__(self):
        return f" Mathoperation : {self.x}, {self.y}"
    
# Object creation 
mathOperation = MathOperation(7, 6)
#function call
print(mathOperation.add())
print(mathOperation.sub())
print(mathOperation.mul())
print(mathOperation.div())

print(mathOperation)
  
    
