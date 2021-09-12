import random
def hangman():

    word = random.choice(["animals","vegetables","fruits","food","foodlover","cusine","fan","pc","laptop","monitor"])
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guesses = ''

    while len(word) > 0:
        main = ""
        missed = 0
        # loop for if the word from word_list then it will update the main with new letter
        for letter in word:
            if letter in guesses:
                main = main + letter
                #else none
            else:
                main = main + "_" + " "

        if main == word:#if you successfully find the word you will be winner
            print(main)
            print("you won!")
            break
        print ("Guess the word" ,main )
        guess = input()

# guess is a user input that we are going to take
        if guess in valid_letters: # search that guess word in valid letters
            guesses = guesses + guess # if yes then add then add the guess word in guesses
        else:
            print("you made a typo")
            guess = input()
        #if the guess the word not in word list then turn will reduced
        if guess not in word:
             turns = turns - 1
             if turns == 9:
                 print(" 9 turns are left")
                 print("  ------ ")
             if turns == 8:
                print("8 turns are left")
                print("   ------   ")
                print("     0      ")
             if turns == 7:
                print("7 turns are left")
                print("    ------  ")
                print("      0     ")
                print("      |     ")
             if turns == 6:
                print("6 turns are left")
                print("    ------  ")
                print("      0     ")
                print("      |     ")
                print("     /      ")
             if turns == 5:
                print(" 5 turns are left ")
                print("    ------  ")
                print("      0     ")
                print("      |     ")
                print("     / \     ")
             if turns == 4:
                print(" 4 turns are left ")
                print("    ------  ")
                print("     \O     ")
                print("      |     ")
                print("     / \     ")
             if turns == 3:
                print(" 3 turns are left ")
                print("    ------  ")
                print("     \O/      ")
                print("      |     ")
                print("     / \     ")
             if turns == 2:
                print(" 2 turns are left ")
                print("    ------  ")
                print("     \O/|      ")
                print("      |     ")
                print("     / \     ")
             if turns == 1:
                print(" 1 turns are left ")
                print("you only have turn left")
                print("    ------  ")
                print("     \O_|/   ")
                print("      |     ")
                print("     / \     ")
             if turns == 0:
                print("Game Over")
                print("you loose!")
                print("    ------  ")
                print("      0_|   ")
                print("     /|\     ")
                print("     / \     ")
                break





name = input("What's Your name ")
print ("Welcome" , name , "\nfor this hangman game")
print ("|----------------------|")
print ("you have 10 chances to complete the word.\nSo let's enroll ")
hangman()
print()
