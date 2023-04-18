# Stage 4/8: Help is on the way
import random


print("H A N G M A N")
words = ("python", "java", "swift", "javascript")
word = random.choice(words)
guessed_word = input(f"Guess the word {word[:3] + '-' * (len(word) - 3)}")
print("You survived!" if guessed_word == word else "You lost!")
