"""
Python basics, Problem Set, hangman.py
Name: TODO
Collaborators: TODO
Time spent: TODO
"""

# ---------------------------------------------------------------------------- #
#                                 Hangman Game                                 #
# ---------------------------------------------------------------------------- #


# -------------------------------- Helper code ------------------------------- #
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    with open(WORDLIST_FILENAME, "r") as inFile:
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# ---------------------------- end of helper code ---------------------------- #


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far, assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed, False otherwise
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    list_of_secret_word=[] 
    for i in secret_word:
        list_of_secret_word.append(i)
    for j in letters_guessed:
        if j in list_of_secret_word:
            list_of_secret_word.remove(j) 
    if list_of_secret_word==[]:
        return True
    else:
        return False
    
    
    


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
        which letters in secret_word have been guessed so far.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    hidden_secret_word=''
    list_of_hidden_secret_word=[]
    for i in range(len_secret_word):
        list_of_hidden_secret_word.append("*")
    for x in letters_guessed:
        for j in range(len_secret_word):
            if secret_word[j]==x:
                list_of_hidden_secret_word[j]=x
                hidden_secret_word=''.join(list_of_hidden_secret_word)
    return hidden_secret_word



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters=string.ascii_lowercase
    list_available_letters=[]
    for i in available_letters:
        list_available_letters.append(i)
    for j in letters_guessed:
        if j in list_available_letters:
            list_available_letters.remove(j)
    available_letters=''.join(list_available_letters)
    return available_letters



def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
    partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    number_guesses=6
    number_warnings=3
    score=0
    is_vowels = {'a', 'e', 'i', 'o'}
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " +str(len_secret_word) +" letters long.")
    print("You have " +str(number_warnings) +" warnings left.")
    print("-------------")
    while(is_word_guessed(secret_word, letters_guessed)==False):
        
        if number_guesses==1:
            print("You have " +str(number_guesses) +" guess left.") #singular 
        else:
            print("You have " +str(number_guesses) +" guesses left.") #plural
        print("Available letters:" +get_available_letters(letters_guessed))
        user_input=''
        user_input_list=[]
        #check user input a single letter
        while True:
            user_input = input('Please guess a letter: ')
            if len(user_input) == 1:
                break
            else:
                print('Please guess a single letter.')
                continue
        user_input=user_input.lower()
        #save all character user input to a list
        user_input_list.append(user_input)
        #check if user input invalid letter
        if user_input.isalpha()==False: 
            number_warnings=number_warnings-1
            if number_warnings==0 or number_warnings==1:
                print("Oops! That is not a valid letter. You have " +str(number_warnings) +" warning left:" +get_guessed_word(secret_word, letters_guessed)) #singular
            elif number_warnings==-1:
                print("Oops! That is not a valid letter. You have no warning left:" +get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That is not a valid letter. You have " +str(number_warnings) +" warnings left:" +get_guessed_word(secret_word, letters_guessed)) #plural
        #check if user input a letter that has already been guessed
        elif user_input in user_input_list[:-1] or user_input in letters_guessed:
            number_warnings=number_warnings-1
            if number_warnings==0 or number_warnings==1:
                print("Oops! You've already guessed that letter. You have "+str(number_warnings)+" warning left:" +get_guessed_word(secret_word, letters_guessed))
            elif number_warnings==-1:
                print("Oops! You've already guessed that letter. You have no warning left:" +get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have " +str(number_warnings) +" warnings left:" +get_guessed_word(secret_word, letters_guessed))
        # check if user input a letter that correct in secret_word
        elif user_input in secret_word:
            letters_guessed.append(user_input)
            print("Good guess:" +get_guessed_word(secret_word, letters_guessed))
            #check if the secret_word is guessed
            if is_word_guessed(secret_word, letters_guessed)==True:
                print("Congratulations, you won!")
                score=number_guesses*number_unique_letters_in_secret_word(secret_word)
                print("Your total score for this game is:" +str(score))
                break
        # check if user input a lettet that not in the secret word    
        else:
            if user_input in is_vowels:
                number_guesses=number_guesses-2
            else:
                number_guesses=number_guesses-1
            print("Oops! That letter is not in my word.")
            print("Please guess a letter:" +get_guessed_word(secret_word, letters_guessed))
        print ("-------------")
        #game over when user run out of number_guesses or number_warnings
        if number_warnings<=-1 or number_guesses<=0:
            print("Sorry, you ran out of guesses. The word was else.")
            break
    
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# ---------------------------------------------------------------------------- #


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    list_my_word=[]
    list_other_word=[]
    if len(my_word)!= len(other_word):
        return False
    else:
        for x in range(len(other_word)):
            list_other_word.append(other_word[x])
        for y in range(len(my_word)):
            list_my_word.append(my_word[y])
        for i in range(len(list_my_word)):
            if list_my_word[i]=='*' and list_other_word[i] not in list_my_word:
                list_other_word[i]="*"
        if list_other_word==list_my_word:
            return True
        else:
            return False


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word

    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.

    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    list_possible_matches=[]
    word_possible_matches=''
    
    for j in wordlist:
        if match_with_gaps(my_word,j)==True:
            list_possible_matches.append(j)
    word_possible_matches=' '.join(list_possible_matches)
    return word_possible_matches
    



def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
    partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
    matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    number_guesses=6
    number_warnings=3
    score=0
    is_vowels = {'a', 'e', 'i', 'o'}
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " +str(len_secret_word) +" letters long.")
    print("You have " +str(number_warnings) +" warnings left.")
    print("-------------")
    while(is_word_guessed(secret_word, letters_guessed)==False):
        
        if number_guesses==1:
            print("You have " +str(number_guesses) +" guess left.") #singular 
        else:
            print("You have " +str(number_guesses) +" guesses left.") #plural
        print("Available letters:" +get_available_letters(letters_guessed))
        user_input=''
        user_input_list=[]
        #check user input a single letter
        while True:
            user_input = input('Please guess a letter: ')
            if len(user_input) == 1:
                break
            else:
                print('Please guess a single letter.')
                continue
        user_input=user_input.lower()
        #save all character user input to a list
        user_input_list.append(user_input)
        #input "*" with hint
        if user_input=='*':
            print('Possible word matches are: '+show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        #check if user input invalid letter
        elif user_input.isalpha()==False: 
            number_warnings=number_warnings-1
            if number_warnings==0 or number_warnings==1:
                print("Oops! That is not a valid letter. You have " +str(number_warnings) +" warning left:" +get_guessed_word(secret_word, letters_guessed)) #singular
            elif number_warnings==-1:
                print("Oops! That is not a valid letter. You have no warning left:" +get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That is not a valid letter. You have " +str(number_warnings) +" warnings left:" +get_guessed_word(secret_word, letters_guessed)) #plural
        #check if user input a letter that has already been guessed
        elif user_input in user_input_list[:-1] or user_input in letters_guessed:
            number_warnings=number_warnings-1
            if number_warnings==0 or number_warnings==1:
                print("Oops! You've already guessed that letter. You have "+str(number_warnings)+" warning left:" +get_guessed_word(secret_word, letters_guessed))
            elif number_warnings==-1:
                print("Oops! You've already guessed that letter. You have no warning left:" +get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have " +str(number_warnings) +" warnings left:" +get_guessed_word(secret_word, letters_guessed))
        # check if user input a letter that correct in secret_word
        elif user_input in secret_word:
            letters_guessed.append(user_input)
            print("Good guess:" +get_guessed_word(secret_word, letters_guessed))
            #check if the secret_word is guessed
            if is_word_guessed(secret_word, letters_guessed)==True:
                print("Congratulations, you won!")
                score=number_guesses*number_unique_letters_in_secret_word(secret_word)
                print("Your total score for this game is:" +str(score))
                break
        # check if user input a lettet that not in the secret word    
        else:
            if user_input in is_vowels:
                number_guesses=number_guesses-2
            else:
                number_guesses=number_guesses-1
            print("Oops! That letter is not in my word.")
            print("Please guess a letter:" +get_guessed_word(secret_word, letters_guessed))
        print ("-------------")
        #game over when user run out of number_guesses or number_warnings
        if number_warnings<=-1 or number_guesses<=0:
            print("Sorry, you ran out of guesses. The word was else.")
            break


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
def number_unique_letters_in_secret_word(secret_word):
    number_unique=[]
    for i in secret_word:
        number_unique.append(i)
    number_unique=set(number_unique)
    return len(number_unique)


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    secret_word = choose_word(wordlist)
    letters_guessed=[]
    len_secret_word=len(secret_word) #length of secret word
    hangman(secret_word)

# ---------------------------------------------------------------------------- #

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
