#create a class called Rectangle that has two attributes: length and width. the class should have a method to calculate the area of the rectangle and another method to calculate the perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(f"Area of rectangle: {self.length * self.width}")
    
    def perimeter(self):
        print(f"Perimeter of rectangle: {2 * (self.length + self.width)}")


l = int(input("Enter length of rectangle: "))
w = int(input("Enter width of rectangle: "))
obj = Rectangle(l, w)
obj.area()
obj.perimeter()