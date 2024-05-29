class Person:#Create the class where the objects will be created
  def __init__(self, name, age):#Initialize varibles 
    self.name = name
    self.age = age

p1 = Person("John", 36)#Take the input

print(p1.name)#Display the output
print(p1.age)
