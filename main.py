import random
import string


while True:
    print("H A N G M A N")
    play = input('Type "play" to play the game, "exit" to quit:')
    if play == "play":
        words_list = ['python', 'java', 'kotlin', 'javascript']
        word = random.choice(words_list)
        player = "-" * len(word)
        life = 8
        guessed_letters = []
        while life > 0:
            print()
            print(player)
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print("You should input a single letter")
                continue
            if letter not in string.ascii_lowercase:
                print("Please enter a lowercase English letter")
                continue
            if letter in guessed_letters:
                print("You've already guessed this letter")
            elif letter in word:
                player = list(player)
                idx = 0
                for i in word:
                    if i == letter:
                        player[idx] = letter
                    idx += 1
                player = "".join(player)
            else:
                print("That letter doesn't appear in the word")
                life -= 1
            guessed_letters.append(letter)
            if player == word:
                print("You guessed the word!\nYou survived!")
                break
        else:
            print("You lost!")
        continue
    else:
        break
