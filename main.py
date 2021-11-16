import random


# Write your code here
print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(word_list)
hint = "-" * len(guess_word)
for i in range(8):
    print(hint)
    guess_letter = input("Input a letter: ")
    hint = list(hint)
    letters_guess_word = set(guess_word)
    if guess_letter in letters_guess_word:
        index = 0
        for spell in guess_word:
            if spell == guess_letter:
                hint[index] = guess_letter
            index += 1
    else:
        print("That letter doesn't appear in the word")

    hint = ''.join(hint)
    print("")

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
