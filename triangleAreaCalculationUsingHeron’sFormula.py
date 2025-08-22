
print(2*3)
print(2**3)

a= int(input("Enter a First Side: "))
b = int (input("Enter a Second Side: "))
c= int(input("Enter a Third Side: "))
s = (a+b+c)/2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"The area of the triangle is {area}.")