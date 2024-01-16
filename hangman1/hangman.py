import random
import string

from words import words
from hangman_visual import lives_visual_dict


def check_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word

def hangman():
    secret_word = check_valid_word(words).upper()
    secret_letter = set(secret_word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    lives = 7

    while len(secret_letter) > 0 and lives > 0:
        print(f"You have {lives} lives and used these letter", " ".join(used_letter))
        print(" ".join([letter if letter in used_letter else "-" for letter in secret_word]))
        user_letter = input("Enter a letter to guess: \n").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in secret_letter:
                secret_letter.remove(user_letter)
            else:
                lives -= 1
                print(lives_visual_dict[lives])
                print(" ")
        elif user_letter in used_letter:
            print("You already used that letter")
        else:
            print("That is not valid letter")

    if lives == 0:

        print(f"You loose! {secret_word}")
    else:
        print(f"You win!!!!", secret_word)


hangman()