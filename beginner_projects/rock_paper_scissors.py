import random 

#computer's rock paper scissor choice
computer_choice = random.choice([1,2,3])

#Welcome message to start game
print("1:Yes; 2:No\nWelcome, Would you like to play rock, paper, scissors?:", end=" ")
play_choice = int(input())
print("\t~~~~~~~~~~~~")

if play_choice ==1:
    play_choice == True

while play_choice == 1:
    #Prompt user 
    print("1: Rock; 2: Paper; 3: Scissor\nWhat is your choice?:", end=" ")
    user_choice = int(input())
    print("\t~~~~~~~~~~~~")

    #logic to see if you beat computer
    #Draws
    if computer_choice == 1 and user_choice == 1:   
        print("Draw, both picked Rock")
    elif computer_choice == 2 and user_choice == 2:   
        print("Draw, both picked Paper")
    elif computer_choice == 3 and user_choice == 3:   
        print("Draw, both picked Scissors")
    #computer wins
    elif computer_choice == 1 and user_choice == 3:   
        print("Computer: Rock | User: Scissors")
        print("Computer wins!")
    elif computer_choice == 3 and user_choice ==2:   
        print("Computer: Scissors | User: Paper")
        print("Computer wins!")
    elif computer_choice == 2 and user_choice == 1:   
        print("Computer: Paper | User: Rock")
        print("Computer wins!")
    #User wins
    elif computer_choice == 3 and user_choice == 1:   
        print("Computer: Scissors | User: Rock")
        print("User wins!")
    elif computer_choice == 2 and user_choice ==3:   
        print("Computer: Paper | User: Scissors")
        print("User wins!")
    elif computer_choice == 1 and user_choice == 2:   
        print("Computer: Rock | User: Paper")
        print("User wins!")
    else:
        print("Invalid Input")

#######DDEBUG QUIT OPTION
    #check if player still wants to play
    print("\t~~~~~~~~~~~~")
    print("1:Yes; 2:No\nWould you like to continue playing?:", end=" ")
    play_choice == int(input())
    if play_choice ==2:
        break
