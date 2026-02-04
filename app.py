import random
from country_list import country_list
from contry_and_capital_list import countries_and_capitals
from ascii import stages



def difficulty():
    print("Choose difficulty:")
    print("1 - Easy (5 lives)")
    print("2 - Hard (4 lives + Countries and their capitals)")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            return country_list, 5
        elif choice == "2":
            return countries_and_capitals(), 4  
        else:
            print("Invalid choice.")
    
def display_of_word(word, revealed_letter):
    display = []
    for char in word:
        if char.lower() in revealed_letter:
            display.append(char)
        else:
            display.append("_")
    return " ".join(display)

def get_guess():
    guess = input("Guess a letter (or type 'quit'): ").strip()
    if guess.lower() == "quit":
        return "quit"
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        return None
    return guess.lower()


def is_word_revealed(word, revealed_letters):
    return all(char.lower() in revealed_letters for char in word)


#the actual game part


def play_game():
    word_pool, lives = difficulty()
    word = random.choice(word_pool)

    revealed_letters = set()
    wrong_letters = set()
    guessed_letters = set()
    picture_counter = 0 
    
    print("\nLet's play Hangman!\n")

    while True: 
        print(stages[picture_counter])
        print("Word:", display_of_word(word, revealed_letters))
        print("Wrong guesses:", " ".join(sorted(wrong_letters)))
        print(f"Lives left: {lives}\n")

        guess = get_guess()
        if guess == "quit":
            print("Buhbyeeee!")
            return
        if guess is None:
            continue

        if guess in guessed_letters:
            print("You already guessed that letter you silly goose!")
            print(f"Lives unchanged: {lives}\n")
            continue

        guessed_letters.add(guess)

        if guess in word.lower():
            revealed_letters.add(guess)
            print("Good! The letter is in the word! :3")
            print(f"Lives remaining: {lives}\n")
        else:
            wrong_letters.add(guess)
            lives -= 1
            picture_counter += 1
            print("Wrongg! :/ ")
            print(f"You lost a life! Lives remaining: {lives}\n")

        if is_word_revealed(word, revealed_letters):
            print("Congratulations! You won! :D ")
            print("The word was:", word)
            return

        if lives <= 0:
            print(stages[-1])
            print("You lost! :(")
            print("The word was:", word)
            return


if __name__ == "__main__":
    play_game()
       


