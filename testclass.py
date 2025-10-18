# w3school
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("John", 36)
print(p1.name)
print(p1.age)

# The __init__() method is called automatically every time the class is being used to create a new object.