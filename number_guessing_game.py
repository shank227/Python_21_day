import random

Max_number = int(input("Enter a digit: - "))

if Max_number <= 0:
    print("Please Enter a number greater than 0")
    quit()

random_number = random.randint(0, Max_number)
guesses = 0

username = input("Username: ")

while True:
    guesses += 1
    user_guess = int(input("Please make a guess: - "))
    if user_guess == random_number:
        print("Good Job correct answer!!")
        break
    elif user_guess>random_number:
        print("You were above the number;\n hint: guess below your entered number!!")
    else:
        print("You were below the number;\n hint: guess above your entered number!!")

if guesses == 1:
    print("Good job", username, "You guessed it in 1 go!!!")

else:
    print("Good Job", username, "you got it in", guesses, "guesses!!")