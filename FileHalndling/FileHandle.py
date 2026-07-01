# Name mangaling example 
class FileHandle :
    def __init__(self):
        self.__name = "vikash"
    def get_name(self) :
        return self.__name

fileHandle = FileHandle()

## Private variable can be access 
# using name mangaling
print(fileHandle._FileHandle__name)



# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))

for i in range(5):
  print(i)