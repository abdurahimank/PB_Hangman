import random

# Write your code here
print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(word_list)
player_guess = input("Guess the word:")
if player_guess == guess_word:
    print("You survived!")
else:
    print("You lost!")
