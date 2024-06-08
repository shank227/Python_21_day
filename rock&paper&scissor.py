import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("rock/paper/scissors shoo or 'q' to quit: ")
    if user_input == "q":
        break

    if user_input not in choices:
        continue

    random_computer_choice = random.randint(0, 2)

    computer_pick = choices[random_computer_choice]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!!")
        user_wins+=1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!!")
        user_wins+=1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!!")
        user_wins+=1
    
    else:
        print("You lost:(((")
        computer_wins+=1

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Goodbye and Thanks for playing")
    