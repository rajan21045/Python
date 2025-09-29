num = int(input("Enter a number: "))
count = 0
while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
    print(num)
    count +=1

print(f"Total steps: {count}")