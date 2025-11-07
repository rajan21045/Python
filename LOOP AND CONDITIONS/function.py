# # function
# def sum(a,b):
#     sum = a + b
#     print(f"Sum of {a} and {b} is {sum}")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum(a,b)

# WAP that takes three numbers as input and displays the greatest one.

# def greatest(num1, num2, num3):
#     if (num1 > num2 and num1 > num3):
#         print(f"{num1} is the greatest number")
#     elif (num2 > num1 and num2 > num3):
#         print(f"{num2} is the greatest number")
#     else:
#         print(f"{num3} is the greatest number")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# greatest(num1, num2, num3)

# palindrome
# def palindrome(s):
#     if s == s[::-1]:
#         print(f"{s} is a palindrome")
#     else:
#         print(f"{s} is not a palindrome")

# s = input("Enter a string: ")
# palindrome(s)

def palindrome(s):
    while s > 0:
        rem = s%10
        rev = rem+rev*10
        s = s//10
        if s == rev:
            print(f"{s} is a palindrome")
        else:
            print(f"{s} is not a palindrome")

s = int(input("Enter a number: "))
palindrome(s)