# Stage 6/8: The value of life
import random


print("H A N G M A N")
words = ("python", "java", "swift", "javascript")
word = random.choice(words)
attempt = 8
temp_word = list("-" * len(word))
while attempt > 0:
    print("\n", "".join(temp_word), sep="")
    letter = input("Input a letter: ")
    if letter in temp_word:
        print("No improvements.")
        attempt -= 1
    elif letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                temp_word[i] = letter
    else:
        print("That letter doesn't appear in the word.")
        attempt -= 1
    if "".join(temp_word) == word:
        print("You guessed the word!")
        break
guessed_word = "".join(temp_word)
print("You survived!" if guessed_word == word else "You lost!")
