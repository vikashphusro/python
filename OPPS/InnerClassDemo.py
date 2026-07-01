## Outer class example
class InnerClassDemo :
    def __init__(self):
        self.name = "Outer class"
        
    def display(self) :
        print(f"{self.name}")

    ## Inner class example
    class InnerInnerDemo : 
        def __init__(self):
            self.name = "Inner class"
        def display(self) :
            print(f"{self.name}")

## Object of outer class
innerClassDemo = InnerClassDemo()
innerClassDemo.display()
## Object of inner class
innerInnerDemo = innerClassDemo.InnerInnerDemo()
innerInnerDemo.display()
