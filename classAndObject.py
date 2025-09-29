# class
class Calculator:
    def add(self, x, y):
        print(f"The sum of {x} and {y} is {x + y}")
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def float_divide(self, x, y):
        return x / y

obj = Calculator()
obj.add(5, 3)
sub = obj.subtract(10, 4)
print(f"The difference is {sub}")
mul = obj.multiply(2, 6)
print(f"The product is {mul}")
float_div = obj.float_divide(8, 2)
print(f"The float division result is {float_div}")


# inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def first(self):
        print("i am a student")
    

obj1 = Person("Alice", 30)
obj1.display()

obj2 = Student("Bob", 20)
obj2.display()
obj2.first()

class Bird:
    def type(self):
        print("There are many types of bird")
class Parrot(Bird):
    def color(self):
        print("Parrots are usually green in color")
class Penguin(Bird):
    def color(self):
        print("Penguins are usually black and white in color")
class Sparrow(Bird):
    def color(self):
        print("Sparrows are usually brown in color")

obj1 = Parrot()
obj1.type()
obj1.color()
obj2 = Penguin()
obj2.type()
obj2.color()
