# Stage 7/8: Error!
import random
import string


print("H A N G M A N")
words = ("python", "java", "swift", "javascript")
word = random.choice(words)
attempt = 8
temp_word = list("-" * len(word))
already_guessed = set()
while attempt > 0:
    while True:
        print("\n", "".join(temp_word), sep="")
        letter = input("Input a letter: ")
        if len(letter) == 1:
            if letter in string.ascii_lowercase:
                break
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        print("Please, input a single letter.")
    if letter in already_guessed:
        print("You've already guessed this letter.")
    elif letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                temp_word[i] = letter
    else:
        print("That letter doesn't appear in the word.")
        attempt -= 1
    already_guessed.add(letter)
    if "".join(temp_word) == word:
        print(f"You guessed the word {word}!")
        break
guessed_word = "".join(temp_word)
print("You survived!" if guessed_word == word else "You lost!")
