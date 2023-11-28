import random

def choose_word():
    word_list = ['python', 'java', 'javascript', 'php']
    return random.choice(word_list)

def display_intro():
    print("HANGMAN")

def display_word_hint(word, guessed_letters):
    hint = ''
    for letter in word:
        if letter in guessed_letters:
            hint += letter
        else:
            hint += '-'
    return hint

def play_game():
    secret_word = choose_word()
    guessed_letters = []
    attempts_left = 8

    while attempts_left > 0:
        hint = display_word_hint(secret_word, guessed_letters)
        print(hint)

        if '-' not in hint:
            print("You guessed the word", secret_word + "!")
            print("You survived!")
            return

        guess = input("Input a letter: > ")

        if len(guess) != 1 or not guess.isalpha() or not guess.islower():
            print("Please enter a lowercase English letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue

        if guess not in secret_word:
            print("That letter doesn't appear in the word")
        else:
            print("No improvements")

        guessed_letters.append(guess)
        attempts_left -= 1

    print("You lost!")

def main_menu():
    while True:
        display_intro()
        print("Type 'play' to play the game, 'exit' to quit:")
        choice = input("> ")

        if choice == 'play':
            play_game()
        elif choice == 'exit':
            break
        else:
            print("Invalid choice. Please type 'play' or 'exit'.")

if __name__ == "__main__":
    main_menu()
