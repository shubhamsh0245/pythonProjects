
import random

print("---------------------------------------------------------------------------")
print("$$ This Is A Word Guessing Game $$")
print("---------------------------------------------------------------------------")
print("In This Computer Will Choose A Word. Then You Have To Guess The Alphabets ^o^")
print("---------------------------------------------------------------------------")

words = ["apple", "monkey", "orange", "python", "wizard", "mountains", "banana"]
word = random.choice(words)

wordLength = len(word)

ans = ["-" for i in range(0,wordLength)]

user_name = input("What Is Your Good Name?\n")
print("\nWelcome!", user_name)
print("Now Guess The Alphabets")

attempts = random.randrange(10, 15)

print("I Decided To Give You", attempts, "attempts. Good Luck!")
attempt = 0

while True:
    attempt += 1
    if attempt > attempts:
        print("Oh! No More Attempts. You Loose the word was", word)
        break

    if word == ''.join(ans):
        print("You Won! The Word Is", word.title())
        break
    
    for i in ans:
        print(i)
    
    user_choice = input("Enter The Alphabet --> ")

    if user_choice in word:
        for i in range(0,wordLength):
            if word[i] == user_choice:
                ans[i] = user_choice
