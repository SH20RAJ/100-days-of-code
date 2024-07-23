

import random 

word_list = ["aardvark", "baboon", "camel", "dog", "elephant", "frog", "goat", "hippopotamus", "iguana", "jaguar", "kangaroo", "lion", "monkey", "nightingale", "octopus", "penguin", "python", "queen", "rabbit", "snake", "tiger", "unicorn", "vampire", "wolf", "xylophone", "yak", "zebra"]

word = random.choice(word_list)


print (f"Your word is {word}")
display = []
for i in range(len(word)):
    display.append("_")

print(display)



chances = len(word) 


for i in range(len(word)):
    if chances <= 0:
        print("you lost")
        break
    guess = input("Enter Guess : ")

    for i in range(len(display)):
        if(guess == word[i]):
            display[i] = guess
        else:
            chances = chances - 1
    
    print(display)

print("you won")