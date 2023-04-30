
import random

print("-----------------------------------------------------------")
print("$$ Welcome! To This Number Guessing Game Built In Python $$")
print("-----------------------------------------------------------")
print("To Play This Game You Have To Give Me A Range. I Will Select Random Number From It And You Have To Guess ^o^")
print("----------------------------------------------------------")

print("Enter Range \n")


A = int(input("From: "))
B = int(input("To: "))

try:
    ans = random.randrange(A,B)

except:
    print("An Error Occured!")

else:

    chances = random.randrange(2,6)
    print("You Only Have", chances, "Chance To Guess")
    
    attempts = 0

    while attempts <= chances:

        if attempts == chances:
            print("\nNo More Attempts, You Loose!")
            break
        
        user_input = int(input("Guess The Number :"))


        if user_input > ans:
            print("High! Think Low")
        
        elif user_input < ans:
            print("Low! Think High")

        else:
            print("You Guessed It In", attempts, "attempts")
            break

        attempts += 1

finally:
    print("Exiting Program...")
