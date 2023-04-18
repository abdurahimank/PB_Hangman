# Stage 5/8: Keep trying
import random


print("H A N G M A N")
words = ("python", "java", "swift", "javascript")
word = random.choice(words)
attempt = 8
temp_word = list("-" * len(word))
while attempt > 0:
    attempt -= 1
    print("\n", "".join(temp_word), sep="")
    letter = input("Input a letter: ")
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                temp_word[i] = letter
    else:
        print("That letter doesn't appear in the word.")
    # if "".join(temp_word) == word:
       # break
# guessed_word = "".join(temp_word)
# print("You survived!" if guessed_word == word else "You lost!")
print("Thanks for playing!")
