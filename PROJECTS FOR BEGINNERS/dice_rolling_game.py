import random
counter=0
while True:
    choice = input("Roll The Dice? (y/n): ").lower()
    if(choice == 'y'):
        choice2 = int(input("How Many Dice You Want To Roll: "))
        roll = []
        for _ in range(choice2):
            roll.append(random.randint(1,6))
        counter+=1
        print(tuple(roll))
        print(f"You Have Rolled The Dice During The Session Is {counter}.")
    elif choice == 'n':
        print('Thank You For Playing!!')
        print(f"You Have Rolled The Dice During The Session Is {counter}.")
        break
    else:
        print("Invalid Choice. Please Enter The Valid Choice. Thank You!!")