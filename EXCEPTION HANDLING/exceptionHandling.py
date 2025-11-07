# exception handling example
a = int(input("Enter the numerator: "))
b = int(input("Enter the denominaotr: "))

try:
    r = a / b
    print(f"The result of {a} divided by {b} is {r}.")
except:
    print("Error: Division by zero is not allowed.")
finally: 
    print("This is the final code block that should be run at any cost")