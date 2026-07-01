########## Class example in python ##############

class HelloWorld :
    xyx = "vikash"
    def __init__(self, name, number = 1000):
       self.name = name
       self.number = number

    def display_data(xx) :
       print(f"Name is {xx.name}, Number is {xx.number}")

class HelloWorldDemo :
  pass

class MultiHelloWorld :
   def __init__(self, id,  domain, code, pin):
      self.id = id
      self.domain = domain
      self.code = code 
      self.pin = pin

   def display_self_name(self):
      print("Hi Vikash how are u?")
    
   def display_whole_data(self) :
      print(f"id : {self.id}")
      print(f"domain : {self.domain}")
      print(f"code : {self.code}")
      print(f"pin : {self.pin}")
      self.display_self_name()

##### Object creation of class ##########
hello = HelloWorld("rajesh")
hello.display_data()

hello_world = HelloWorld("vikash", 4000)
hello_world.display_data()
print("XYZ : " + hello_world.xyx)
hello_world.xyx = "Rajesh"
print(f"XYZ formatted version : {hello_world.xyx}")
hello_world_demo = HelloWorldDemo()
hello_world_demo .name = "akash"
hello_world_demo.data = 2000
print("Pass class example and value of name :" + hello_world_demo.name)
print(f"pass class another value is  : {hello_world_demo.data}")

multiHelloWorld = MultiHelloWorld(1, "quik.com", 200, 829144)

multiHelloWorld.pin = 560066
multiHelloWorld.display_whole_data()