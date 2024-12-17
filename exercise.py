print("------INSTRUCTION ONE--------")
player_name = input("Enter your username to begin playing: \n").strip().upper() 
# the .strip() is used to remove any white spaces from the input, and .upper() is used to convert the input to uppercase. This is useful especially since we do not know what the user might input to the program, hence saving us from a crashing program
print(f"Welcome to the paradox of minds, {player_name}!\n")

print("--------Intuition Test-------- \n")
print("Trust your gut only !!!")

print("------INSTRUCTION TWO--------\n")
print("To begin, please choose a random number between 0 and 9.\n")

# Input validation for random number selection
while True:
    try:
        random_num = int(input("Pick your random number: \n"))
        if 0 <= random_num <= 9:
            break
        else:
            print("Please enter a number between 0 and 9.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

print(f"You have chosen the number {random_num}.\n")

# Function definitions
def choice_zero():
    print("Which number comes next in the sequence?")
    print("2, 4, 8, 16, ...\n")
    print("A) 28")
    print("B) 32")
    print("C) 24")
    print("D) 64")
    zero = input("Enter your choice: \n").strip().upper()
    if zero == "B":
        print("Correct!")
    else:
        print("Incorrect!")

def choice_one():
    print("Which word feels most connected to the given word: Ocean?\n")
    print("A) Vast")
    print("B) Sky")
    print("C) Mountain")
    print("D) Storm")
    one = input("Enter your choice: \n").strip().upper()
    if one == "A":
        print("Correct!")
    else:
        print("Incorrect!")

def choice_two():
    print("Imagine you saw a picture of a table. What objects were on it?\n")
    print("A) A lamp, book, and cup")
    print("B) A pen, phone, and keys")
    print("C) A vase, candle, and photo frame")
    print("D) None of the above")
    two = input("Enter your choice: \n").strip().upper()
    if two == "B":
        print("Correct!")
    else:
        print("Incorrect!")

def choice_three():
    print("If a square splits diagonally, which shapes does it create?\n")
    print("A) Two rectangles")
    print("B) Two triangles")
    print("C) Four smaller squares")
    print("D) A circle")
    three = input("Enter your choice: \n").strip().upper()
    if three == "B":
        print("Correct!")
    else:
        print("Incorrect!")

def choice_four():
    print("Which color feels most calming?\n")
    print("A) Blue")
    print("B) Red")
    print("C) Yellow")
    print("D) Black")
    four = input("Enter your choice: \n").strip().upper()
    if four == "A":
        print("Correct!")
    else:
        print("Incorrect!")

def choice_five():
    print("What is the approximate answer to 19 x 21 without calculating?\n")
    print("A) 390")
    print("B) 400")
    print("C) 420")
    print("D) 380")
    five = input("Enter your choice: \n").strip().upper()
    if five == "B":
        print("Correct!")
    else:
        print("Incorrect!")

def choice_six():
    print("Which word doesn't fit in this group?\n")
    print("A) Tree")
    print("B) River")
    print("C) Mountain")
    print("D) Clock")
    six = input("Enter your choice: \n").strip().upper()
    if six == "D":
        print("Correct!")
    else:
        print("Incorrect!")

def choice_seven():
    print("You’re standing at a fork in the road: \nPath one leads into a dense forest. \nPath two winds along a cliff edge.\nWhich path do you feel is safer?")
    print("A) Path one")
    print("B) Path two")
    seven = input("Enter your choice: \n").strip().upper()
    if seven == "A":
        print("Correct!")
    else:
        print("Incorrect!")

def choice_eight():
    print("Imagine a coin toss. What result do you feel will happen?\n")
    print("A) Heads")
    print("B) Tails")
    eight = input("Enter your choice: \n").strip().upper()
    if eight in ["A", "B"]:
        print("Correct!")  # Both options are valid
    else:
        print("Incorrect!")

def choice_nine():
    print("How would someone feel if they lost their wallet?\n")
    print("A) Excited")
    print("B) Calm")
    print("C) Anxious")
    print("D) Inspired")
    nine = input("Enter your choice: \n").strip().upper()
    if nine == "C":
        print("Correct!")
    else:
        print("Incorrect!")

# Main choice handler
def choice(random_num):
    if random_num == 0:
        choice_zero()
    elif random_num == 1:
        choice_one()
    elif random_num == 2:
        choice_two()
    elif random_num == 3:
        choice_three()
    elif random_num == 4:
        choice_four()
    elif random_num == 5:
        choice_five()
    elif random_num == 6:
        choice_six()
    elif random_num == 7:
        choice_seven()
    elif random_num == 8:
        choice_eight()
    elif random_num == 9:
        choice_nine()

# Execute based on user's random number
choice(random_num)
