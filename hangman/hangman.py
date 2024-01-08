import random
import string

from words import words
from hangman_visual import lives_visual_dict


def check_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    secret_word = check_valid_word(words)
    secret_letter = set(secret_word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    lives = 7

    while len(secret_letter) > 0 and lives > 0:
        print(f"You have {lives} lives and used these letter", " ".join(used_letter))
        list_letter = [letter if letter in used_letter else "-" for letter in secret_word]
        print("Current word: ", " ".join(list_letter))
        print(lives_visual_dict[lives])

        user_letter = input("Enter a letter to guess: \n").upper()

        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in secret_letter:
                secret_letter.remove(user_letter)
                print(" ")
            else:
                print(f"{user_letter} is not in the word")
                lives -= 1

        elif user_letter in used_letter:
            print("You already used that letter, try again")
        else:
            print("That is not a valid letter!")

    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"You loosed baby! Stupid! The word is {secret_word}")
    else:
        print(f"You win! The word is {secret_word}")


hangman()
