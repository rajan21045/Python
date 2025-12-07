# Write a function to calculate the nth Fibonacci number.
def fibonacci(num):
    if num<=1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print("Enter a positive integer to find the nth Fibonacci number:")
num = int(input())
result = fibonacci(num)
for i in range(num):
    print(fibonacci(i))