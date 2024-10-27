import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper","scissors"]

print("Welcome! to Rock,Paper,Scissors Game.")

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break

    if user_input not in  choices:
        continue

    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2 
    computer_pick = choices[random_number]
    print("Computer Picked : ", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        

    else:
        print("You lost!")
        computer_wins += 1


print("You won", user_wins,"times.")
print("The computer won",computer_wins,"times.")      

print("Good Bye!🙂")
