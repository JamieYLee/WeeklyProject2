import random

# categories
Animals = ['dog', 'cat', 'tiger', 'lion', 'mouse', 'rabbit', 'fox', 'wolf', 'pig', 'racoon', 'chicken', 'duck']
Fruits = ['apple', 'banana', 'grape', 'peach', 'pear', 'pineapple', 'orange', 'strawberry', 'mango', 'melon',
         'watermelon', 'plum']
Cities = ['losangeles', 'sanfrancisco', 'newyork', 'boston', 'atlanta', 'miami', 'chicago', 'seattle', 'lasvegas',
         'washingtondc', 'houston', 'philadelphia']
Cosmetics = ['eyeshadow', 'eyeliner', 'mascara', 'foundation', 'concealer', 'blush', 'bronzer', 'contouring',
            'hightlighter', 'lipstick', 'lipstain', 'primer']
# random sets from every lists
Random = list(set(Animals + Fruits + Cities + Cosmetics))

# counts how many chances left to play
def count_pic(guess, word):
    if guess == 0:
        print("_________")
        print("|     |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guess == 1:
        print("_________")
        print("|     |")
        print("|     O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guess == 2:
        print("_________")
        print("|     |")
        print("|     O")
        print("|     |")
        print("|     |")
        print("|")
        print("|________")
    elif guess == 3:
        print("_________")
        print("|     |")
        print("|     O")
        print("|    /|")
        print("|     |")
        print("|")
        print("|________")
    elif guess == 4:
        print("_________")
        print("|     |")
        print("|     O")
        print("|    /|\\")
        print("|     |")
        print("|")
        print("|________")
    elif guess == 5:
        print("_________")
        print("|     |")
        print("|     O")
        print("|    /|\\")
        print("|     |")
        print("|    /")
        print("|________")
    # game over
    elif guess == 6:
        print("_________")
        print("|     |")
        print("|     O")
        print("|    /|\\")
        print("|     |")
        print("|    / \\")
        print("|________\n")
        print("YOU LOSE!\n")
        print("The word was '{}'.\n".format(word))
        again_num = int(input("Type 1 to replay or 2 to quit: "))
        if again_num == 1:
              hangman()
        return

# getting words form list above and pick it random
def getwords():
    print("Welcome to Hangman Game!\n")
    category = int(input("Please choose a number of category - 1. Animals / 2. Fruits / 3. Cities / 4. Cosmetics / 5. Random : "))
    if category == 1:
        word = random.choice(Animals)
    elif category == 2:
        word = random.choice(Fruits)
    elif category == 3:
        word = random.choice(Cities)
    elif category == 4:
        word = random.choice(Cosmetics)
    elif category == 5:
        word = random.choice(Random)
    else:
        print("Wrong case!")
    return word

# the main function of playing hangman game
def hangman():
    guess = 0
    word = getwords()
    # making a list from each spelling letters from picked word
    word_list = list(word)

    print("You have {} letters.\n".format(str(len(word))))

    blanks = '_' * len(word)
    blank_list = list(blanks)
    new_blank_list = list(blanks)
    guess_list = []

    count_pic(guess, word)
    print("\n\n" + "" + ' '.join(blank_list) + "\n")

    while guess < 6:
        letter = input("Guess what? ")

        if len(letter) > 1:
            print("Please type just one letter!")
        elif letter == "":
            print("Try keep going this fun game!")
        elif letter in guess_list:
            print("You've already guessed that letter maaaan")
        else:
            guess_list.append(letter)
            i = 0
            while i < len(word):
                if letter == word[i]:
                    new_blank_list[i] = word_list[i]
                i += 1

            if new_blank_list == blank_list:
                print("Beeeppp!!! Wrong answer!!!")
                guess += 1
                count_pic(guess, word)

                if guess < 6:
                    print("Guess again.")
                    print(' '.join(blank_list))

            elif word_list != blank_list:
                blank_list = new_blank_list[:]
                print(' '.join(blank_list))

                if word_list == blank_list:
                    print("Gotcha! You got it!")
                    again_num = int(input("Type 1 to replay or 2 to quit: "))
                    if again_num == 1:
                        hangman()
                    return

                else:
                    print("Great! Think more!")
