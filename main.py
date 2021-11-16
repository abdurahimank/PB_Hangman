import random


# Initiation
print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(word_list)
hint = "-" * len(guess_word)
life = 8

# Main body to check guess word
while life > 0:
    print("")
    print(hint)
    guess_letter = input("Input a letter: ")
    hint = list(hint)
    letters_guess_word = set(guess_word)
    if guess_letter in letters_guess_word:
        index = 0
        if guess_letter not in hint:
            for spell in guess_word:
                if spell == guess_letter:
                    hint[index] = guess_letter
                index += 1
        else:
            print("No improvements")
            life -= 1
    else:
        print("That letter doesn't appear in the word")
        life -= 1

    hint = ''.join(hint)
    if hint == guess_word:
        break

# Final output display
if hint == guess_word:
    print("You guessed the word!")
    print("You survived!")
else:
    print("You lost!")
