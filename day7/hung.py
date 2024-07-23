

import random 

word_list = ["aardvark", "baboon", "camel", "dog", "elephant", "frog", "goat", "hippopotamus", "iguana", "jaguar", "kangaroo", "lion", "monkey", "nightingale", "octopus", "penguin", "python", "queen", "rabbit", "snake", "tiger", "unicorn", "vampire", "wolf", "xylophone", "yak", "zebra"]

word = random.choice(word_list)

print(word)
print("_"*len(word))


guess = input("Enter Guess")
for letter in word:
    if letter == guess:
        print(letter)
    else:
        print("_")

print("game over")

