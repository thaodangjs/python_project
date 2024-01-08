import random


def guess_num():
    secret_num = random.randint(1,10)
    user_num = 0
    time_try = 0
    while user_num != secret_num:
        user_num = int(input("Enter a number between 1 and 10\n"))
        time_try += 1
        if user_num > secret_num:
            print("Too high")
        elif user_num < secret_num:
            print("Too low")
    print(f"You win! You have guessed {secret_num} with {time_try -1} times")

guess_num()
