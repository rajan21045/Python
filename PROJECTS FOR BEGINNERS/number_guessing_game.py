import random
attempt =0
num1 = random.randint(1,100)
while True:
    try:
        choice = int(input("Guess The Number Between 1 And 100: "))
        attempt += 1
        if choice < 1 or choice > 100:
            print("Please enter a number between 1 and 100.")
        elif(num1>choice):
            print("Too Low")
        elif (num1<choice):
            print("Too High")
        else:
            print("Congratulations! You Have Gussed It Right")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")