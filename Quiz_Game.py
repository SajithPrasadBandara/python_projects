#This simple quiz game using python

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okey! Let's play 🙂 ")

score = 0

# First Question
answer = input("What is the longest river in the world? ")
if answer.lower() == "nile river":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'Nile river'.")

# Second Question
answer = input("What is the tallest mountain on Earth? ")
if answer.lower() == "mount everest":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'Mount Everest'.")

# Third Question
answer = input("What is the largest ocean on Earth? ")
if answer.lower() == "pacific ocean":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'Pacific Ocean'.")

# Fourth Question
answer = input("What is the largest desert on Earth?")
if answer.lower() == "antarctic desert":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'Antarctic Desert'.")

# Fifth Question
answer = input("What is the deepest lake on Earth?")
if answer.lower() == "lake bikal":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'Lake Bikal'.")

# How many answers, you got
print("You got "+ str(score)+ " questions correct!")

# How many score, you got
print("You got "+ str((score/5) * 100)+ "% .") 