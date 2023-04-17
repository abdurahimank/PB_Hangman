# Stage 3/8: Make your choice
import random


print("H A N G M A N")
words = ("python", "java", "swift", "javascript")
word = random.choice(words)
guessed_word = input("Guess the word: ")
print("You survived!" if guessed_word == word else "You lost!")
