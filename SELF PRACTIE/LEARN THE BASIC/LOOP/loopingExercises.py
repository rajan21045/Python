import math

# A. Basic for Loop Exercises

# 1. Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)
print("\n")

# 2. Print all even numbers between 1 and 50.
for i in range(1, 51):
    if i%2==0:
        print(i)
print("\n")

# 3. Print all odd numbers between 1 and 50.
for i in range(1, 51):
    if i%2 != 0:
        print(i)
print("\n")

# 4. Print the multiplication table of 5 (up to 10).
for i in range(1, 11):
    print(f"5 * {i}: {5*i}")
print("\n")

# 5. Print numbers from 10 to 1 in reverse order.
for i in range(10, 0, -1):
    print(i)
print("\n")

# B. Basic while Loop Exercises

# 6. Print numbers from 1 to 10 using a while loop.
i = 1
while i<=10:
    print(i)
    i+=1
print("\n")

# 7. Print numbers from 1 to 100 but stop when the number is 50.
while i<=100:
    if i == 50:
        break
    print(i)
    i+=1
print("\n")
# 8. Print the sum of numbers from 1 to 10 using a loop.
j = 1
sum = 0
while j<=10:
    sum+=j
    j+=1
print(f"Sum from 1 to 10 is: {sum}")
print("\n")

# 9. Print all numbers less than 100 that are divisible by 7.
k = 1
while k<100:
    if k%7 == 0:
        print(k)
    k+=1
print("\n")

# 10. Count how many numbers between 1 and 100 are divisible by 5.
count = 0
l = 1
while l<=100:
    if l%5 == 0:
        count+=1
    l+=1
print(f"Count of numbers divisible by 5: {count}")

# C. Pattern Printing (Loops + Logic)

# 11. Print the following pattern:
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*" * i)

# 12. Print the following pattern:
# 54321
# 5432
# 543
# 54
# 5
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end="")
    print()
 
# 13. Print the following pyramid:
#   *
#  ***
# *****
rows = 3
for i in range(1, rows + 1):
    # print spaces
    for space in range(rows - i):
        print(" ", end="")
    
    # print stars
    for star in range(2 * i - 1):
        print("*", end="")
    
    print()

# D. Loop with Conditions

# 14. Print numbers from 1 to 100:
# Print "Fizz" if divisible by 3
# Print "Buzz" if divisible by 5
# Print "FizzBuzz" if divisible by both
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 15. Print all prime numbers between 1 and 50.
# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
# 16. Find and print the factorial of a number entered by the user.
n = 5
result = math.factorial(n)
print(f"The factorial of {n} is {result}")

# E. Loop with Lists
# 17. Given a list:
nums = [10, 20, 30, 40, 50]
# Print each element using a loop.
for i in nums:
    print(i)
print("\n")

# 18. Find the largest number in a list using a loop.
largest = nums[0]
for n in nums:
    if n>largest:
        largest = n
print(largest)
print(max(nums)) 
print("\n")

# 19. Count how many even numbers exist in a list.
countt =0
for i in nums:
    if i%2==0:
        countt+=1
print(countt)
print("\n")

# 20. Reverse a list without using built-in functions.
start = 0
end = len(nums) - 1
while start < end:
    nums[start], nums[end] = nums[end], nums[start]
    start += 1
    end -= 1
print(nums)
