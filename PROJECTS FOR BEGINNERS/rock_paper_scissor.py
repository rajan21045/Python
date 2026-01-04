import random
choice = ('r','p','s')
emoji = {'r':'🪨','p':'📄','s':'✂️'}
while True:
    user_choice = input("Enter Your Choice (r for Rock, p for Paper, s for Scissor): ").lower()
    if user_choice in choice:
        computer_choice = random.choice(choice)
        print(f"Your Choice Is {emoji[user_choice]}  And Computer Choice Is {emoji[computer_choice]}")
        if user_choice == computer_choice:
            print("It's A Tie!")
        elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
            print("You Win!")
        else:
            print("Computer Wins!")
    else:
        print("Invalid Choice. Please Enter r, p, or s.")   
    play_again = input("Do You Want To Play Again? (y/n): ").lower()
    if play_again != 'y':
        print("Thank You For Playing!!")
        break
