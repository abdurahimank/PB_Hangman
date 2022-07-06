import random


print("H A N G M A N")
win = 0
loss = 0
while True:
    mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if mode == "play":
        word_list = ("python", "java", "swift", "javascript")
        word = random.choice(word_list)
        user = "-" * len(word)
        life = 8
        already_guessed = []
        while life > 0:
            print("\n", user, sep="")
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print("Please, input a single letter.")
                continue
            elif letter.isupper() or not letter.isalpha():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if letter in already_guessed:
                print("You've already guessed this letter.")
                continue
            elif letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        user = user[:i] + letter + user[i + 1:]
            else:
                print("That letter doesn't appear in the word.")
                life -= 1
            already_guessed.append(letter)
            if user == word:
                print(f"You guessed the word {user}!", "You survived!", sep="\n")
                win += 1
                break
        if user != word:
            print("\nYou lost!")
            loss += 1
    elif mode == "results":
        print(f"You won: {win} times.", f"You lost: {loss} times.", sep="\n")
    elif mode == "exit":
        break
