import random


# Initiation
print("H A N G M A N")
while True:
    status = input('Type "play" to play the game, "exit" to quit:')
    if status == "play":
        word_list = ['python', 'java', 'kotlin', 'javascript']
        guess_word = random.choice(word_list)
        hint = "-" * len(guess_word)
        life = 8
        already_guessed = set()

        # Main body to check guess word
        while life > 0:
            print("")
            print(hint)
            guess_letter = input("Input a letter: ")
            hint = list(hint)
            letters_guess_word = set(guess_word)
            alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                        "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            if len(guess_letter) == 1:
                if guess_letter in alphabet:
                    if guess_letter in already_guessed:
                        print("You've already guessed this letter")
                    elif guess_letter in letters_guess_word:
                        index = 0
                        already_guessed.add(guess_letter)
                        for spell in guess_word:
                            if spell == guess_letter:
                                hint[index] = guess_letter
                            index += 1
                    else:
                        already_guessed.add(guess_letter)
                        print("That letter doesn't appear in the word")
                        life -= 1
                else:
                    print("Please enter a lowercase English letter")
            else:
                print("You should input a single letter")
            hint = ''.join(hint)
            if hint == guess_word:
                break

        # Final output display
        if hint == guess_word:
            print("You guessed the word!")
            print("You survived!")
            print("")
        else:
            print("You lost!")
            print("")
    elif status == "exit":
        break
    else:
        continue
