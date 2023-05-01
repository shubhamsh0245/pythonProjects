
import random

def banner():
    print("-----------------------------------------")

def turn(computer_turn):
    if computer_turn:
        possibility = 20 - numbers[-1] + 1
        entry = random.randrange(1, possibility)

        print("\nI Am Going To Enter", entry, "Values")

        for i in range(0,entry):
            numbers.append(numbers[-1] + 1)
        
            if numbers[-1]==20:
                print("You Loose!")
                exit()

        print(numbers)
        return False
    
    else:
        print("\nYour Turn.")
        print("\nHow Many Number Do You Wish To Enter?")
        entry = int(input("> "))

        if entry + numbers[-1] > 21:
            print("Not Possible. Now You Can Enter Maximum", 21-numbers[-1], "Number Only.")
            return False
        
        print("Enter Your Values")
        for i in range(0,entry):

            numbers.append(int(input("> ")))

            if numbers[-1] != numbers[-2] + 1:
                print("Your Value Should Be --> Previous Value + 1")
                exit()

            if numbers[-1]==20:
                print("You Win!")
                exit()

        print(numbers)
        return True
    

print()

banner()
print("$$ Welcome To 21 Number Game In Python $$")
banner()
print("\n##### Keep In Mind #####\n")
print("--> If You Enter Value 21. You Will Loose!")
print("--> And The Numbers Should Be In Continuation")
print("--> Now Play The Game And See How It Works.")

print()

print("Do You Want To Start The Game? (Y/N)")
start = input("> ")

if start=='Y' or start=='y':

    numbers = [0]

    print("\nEnter 'F' To Take The First Chance.")
    print("Enter 'S' To Take The Second Chance.")
    chance = input("> ")

    if chance=='S' or chance=='s':
        computer_turn = True
              
    elif chance == 'F' or chance == 'f':
        computer_turn = False

    else:
        print("Select Either S or F")
        exit()
    
    while True:
            computer_turn = turn(computer_turn)
            
else:
    print("Exiting The Game")