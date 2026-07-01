class EncapsulationDemo :
    def __init__(self, name, id):
        self.__name = name
        self.__id = id 
    
    def get_name(self) :
        return self.__name
    
    def set_name(self, name) :
        self.__name = name

    def get_id(self) :
        return self.__id
    
    def set_id(self, id) :
        self.__id = id 

encapsulationDemo = EncapsulationDemo("vikash", 10000)
print(f"Name : {encapsulationDemo.get_name()} ")
print(f"Id : {encapsulationDemo.get_id()} ")
encapsulationDemo.set_name("Rajeev")
encapsulationDemo.set_id(10)
print(f"Name1 : {encapsulationDemo.get_name()} ")
print(f"Id1 : {encapsulationDemo.get_id()} ")
