import random
from functions import *
import time
from chemical import elements
from prettytable import PrettyTable
from colorama import Fore
import sys


def bold(type):
    sys.stdout.write("\033[1m" + type + "\033[0m")

def main():
    print(f"{Fore.GREEN}")
    batman()
    print(f"{Fore.RESET}")
    def check_element_name_and_symbol(name, symbol, missed_elements, user_answers, user_inputs, user_inputs_review):
        for key, value in elements.items():
            if value["name"] == name:
                if value["symbol"] == symbol:
                    return True
                else:
                    missed_elements.append(name)
                    user_answers[name] = value["symbol"]
                    user_inputs[name] = symbol
                    user_inputs_review[name] = [value["symbol"], symbol]
                    return False
        return None

    while True:
        start_time = time.time()
        while True:
            try:
                start_index = int(input(f"{Fore.RESET}Start from (1-{len(elements)}): "))
                if start_index < 1 or start_index > len(elements):
                    print(f"{Fore.RED}Enter a number 1 - {len(elements)}.")
                    continue
                break
            except ValueError:
                print(f"{Fore.RED}Enter a valid number.")

        while True:
            try:
                num_elements = int(input(f"{Fore.RESET}# of elements: "))
                if num_elements > len(elements) - start_index + 1:
                    print(f"{Fore.RED}{len(elements) - start_index + 1} elements max")
                    continue
                break
            except ValueError:
                print(f"{Fore.RED}Enter a valid number.")

        while True:
            order_preference = input(f"{Fore.RESET}In order or randomized: ").lower()
            if order_preference not in ["order", "random", "1"]:
                print(f"{Fore.RED}Enter either 'order' or 'random'")
                continue
            break

        element_keys = list(elements.keys())[start_index - 1:]
        if order_preference == "random":
            random.shuffle(element_keys)
        element_keys = element_keys[:num_elements]

        score = 0
        missed_elements = []
        user_answers = {}
        user_inputs = {}
        user_inputs_review = {}

        for key in element_keys:
            value = elements[key]
            atomic = key
            symbol = value["symbol"]
            name = value["name"]
            user_input_initial = input(f"{Fore.MAGENTA}{name}: ")
            user_input_initial = user_input_initial[0].upper() + user_input_initial[1:]  # Capitalize the first letter
            # question_end_time = time.time()
            result = check_element_name_and_symbol(name, user_input_initial, missed_elements, user_answers, user_inputs,
                                                   user_inputs_review)

            if result is None:
                print(f"{Fore.RED}No element found with the name {name}.")
            if user_input_initial.lower() == "break":
                break
            elif result:
                score += 1

            # elapsed_time = round(question_end_time - start_time, 2)
            # if elapsed_time < 60:
            #     time_taken = f"{elapsed_time} seconds"
            # else:
            #     minutes = int(elapsed_time // 60)
            #     seconds = elapsed_time % 60
            #     time_taken = f"{minutes} minute(s) and {seconds} seconds"


            print(f"{Fore.RESET}-------------")


        if score * 100 / num_elements <= 70:

            bold(f"{Fore.RED}Score: {score}/{num_elements}\n")
        elif score * 100 / num_elements >= 80:

            bold(f"{Fore.GREEN}Score: {score}/{num_elements}\n")
        else:
            bold(f"{Fore.RESET}Score: {score}/{num_elements}\n")
        # print(f"{Fore.RESET}Time taken for the question: {time_taken}")
        timing(start_time)

        try_again_or_review = input(
            f"Try again or Review missed questions? ({Fore.GREEN}try/review{Fore.RESET}): ").lower()
        if try_again_or_review in ["try", "try again"]:
            continue
        elif try_again_or_review in ["review", "review missed", "missed", "question"]:
            for element in missed_elements:
                print(f"Reviewing {element}:")
                user_input2 = input(f"Enter the correct symbol for {element}: ")
                user_input2 = user_input2[0].upper() + user_input2[1:]
                check_element_name_and_symbol(element, user_input2, missed_elements, user_answers, user_inputs,
                                              user_inputs_review)
                print(f"{Fore.RESET}-------------")

        if missed_elements:
            table = PrettyTable()
            table.field_names = ["Element", "Correct", "Your answer"]
            for element in missed_elements:
                table.add_row([element, user_answers[element], user_inputs[element]])
            print("Missed elements:")
            print(table)

        else:
            continue

        if try_again_or_review.lower() == "break":
            break
        else:
            print("Thank you for playing.")
            continue


if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    main()  # Run the main function

    end_time = time.time()  # Record the end time
    elapsed_time = round(end_time - start_time, 2)  # Calculate the elapsed time and round it to 2 decimal places

    if elapsed_time < 60:
        time_taken = f"{elapsed_time} seconds"
    else:
        minutes = int(elapsed_time // 60)
        seconds = elapsed_time % 60
        time_taken = f"{minutes} minute(s) and {seconds} seconds"

    print(f"{Fore.RESET}It took you {time_taken} to take the quiz.")