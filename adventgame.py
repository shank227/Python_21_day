name = input("Enter your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?\n").lower()

while answer == 'left':
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")
    
    if answer == 'swim':
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You have walked for many miles, ran outta water and you lost the game")
    else:
        print("not a valid option you")
        continue

while answer == 'right':
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head hack (cross/back)?\n")

    if answer == 'back':
        print("Go back and Loose")
    
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (Yes/No)\n")

        if answer == 'yes':
            print("You talk to stranger and they take you to their basement and you get captured. Hence LOST")
        
        elif answer == "no":
            print("You ignore the stranger and you are safe. Hence WIN")
        
        else:
            print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")

print("Thank you for trying the game")