import random
from functions import *
from colorama import Fore
from chemical import prefix



def name_to_number_quiz(order):
    keys = list(prefix.keys())
    if order in ["randomized", "random", "r", "2", "Random", "Randomized"]:
        keys = random.sample(keys, len(keys))

    score = 0
    for key in keys:
        user_input = input(f"{Fore.RESET}----------\n{Fore.MAGENTA}{key}: ")
        if user_input == prefix[key]:
            # print("Correct!")
            score += 1
        # else:
            # print(f"Wrong! The correct answer is {prefix[key]}.")

    print(f"\nScore: {score}/{len(keys)}")

def number_to_name_quiz(order):
    keys = list(prefix.keys())
    if order in ["randomized", "random", "r", "2", "Random", "Randomized"]:
        keys = random.sample(keys, len(keys))

    score = 0
    for key in keys:
        user_input = input(f"{Fore.RESET}----------\n{Fore.MAGENTA}{prefix[key]}: ")
        if user_input.lower() == key.lower():
            # print("Correct!")
            score += 1
        # else:
        #     print(f"Wrong! The correct answer is '{key}'.")

    print(f"\nScore: {score}/{len(keys)}")

def main():
    conversion_type = input(f"1 ; name to number\n2 ; number to name\n{Fore.GREEN}Option: ").lower()
    quiz_order = input(f"{Fore.RESET}1 ; Order\n2 ; Random\n{Fore.GREEN}Option: ").lower()

    if conversion_type in ["name to number", "1"]:
        start_timing = time.time()
        name_to_number_quiz(quiz_order)
        timing(start_timing)
    elif conversion_type in ["number to name", "2"]:
        start_timing = time.time()
        number_to_name_quiz(quiz_order)
        timing(start_timing)


if __name__ == "__main__":
    main()
