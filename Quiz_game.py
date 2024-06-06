print("\t\t\t\tWelcome to Quizzy Braniacs\t\t\t\t")
print("\t\t\t\tCreated by Shashank Bakshi\t\t\t\t")

## Options to choose
print("\n1. Start")
print("2. Instructions")
print("3. Exit")

## counter for initialinzing score in the game
score = 0

## Input to choose the option
option = int(input("Choose the option from above please: "))

## Outcomes of choosing the options with specific control flow statements

## Outcome of selecting Option 1
if option == 1:

    name = input("Enter Your name: ")

    print("Welcome " + name + "!!!Let the games begin!!!")

    print("Question 1. What does RAM stand for?")
    answer = input("Enter your answer: ")
    if answer == "random access memory":
        print('Correct!!')
        score += 1
    else:
        print('Incorrect')
    
    print("Question 2. What is 12 + 19?")
    answer = int(input("Enter your answer: "))
    if answer == 31:
        print('Correct!!')
        score += 1
    else:
        print('Incorrect')
    
    print("Question 3. What does GPU stand for?")
    answer = input("Enter your answer: ")
    if answer == "graphics processing unit":
        print('Correct!!')
        score += 1
    else:
        print('Incorrect')
    
    print("Question 4. What is the value of x in the following equation?; 2x + y = 6 where y = 8?")
    answer = int(input("Enter your answer: "))
    if answer == -1:
        print('Correct!!')
        score += 1
    else:
        print('Incorrect')
    
    print("Question 5. What is the value of logical sum of 0 and 1?")
    answer = int(input("Enter your answer: "))
    if answer == 1:
        print('Correct!!')
        score += 1
    else:
        print('Incorrect')
    
    print("\nYou got " + str(score) + " questions correct")
    print("Well " + name + " you have achieved " + str((score/5)*100) + "%. ")

## Outcome of selecting Option 2
elif option == 2:
    print("\t\t\t\t Rules \t\t\t\t")
    print("1. 5 Questions will be asked in an orderly manner related to basics of Computer Science(CS) & Mathematics")
    print("2. The Answer can be typed below the Question")
    print("3. If the answers are correct 1 point the user will recieve; if its wrong 0 point will be recieved")
    print("4. With so on answering the questions, finally your score will be calculated and dsiplayed with your username..")

## Outcome of selecting Option 3
elif option == 3:
    exit()
## Outcome of if any-other option selected instead of available options
else:
    print("Invalid Entry!! Please choose from the options available above...")
