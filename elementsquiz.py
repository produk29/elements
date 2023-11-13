import sys
from prettytable import PrettyTable
from chemical import elements
from functions import *

def bold(tpas):
    sys.stdout.write("\033[1m" + tpas + "\033[0m")


def check_answer(name, symbol, missed_elements, user_answers, user_inputs, user_inputs_review):
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


def print_missed_elements(missed_elements, user_answers, user_inputs):
    table = PrettyTable()
    table.field_names = [f"Element", f"{Fore.GREEN}Correct", f"{Fore.RED}Your answer{Fore.RESET}"]
    table.title = f"{Fore.RESET}{Fore.RED}Missed elements{Fore.RESET}"
    for element in missed_elements:
        table.add_row([element, user_answers[element], user_inputs[element]])
    print(table)


def main():
    batman()
    while True:

        while True:
            try:
                start_index = int(input(f"{Fore.RESET}Start from (1-{len(elements)}): "))
                if str(start_index) == "!=":
                    break
                if start_index < 1 or start_index > len(elements):
                    print(f"{Fore.RED}Enter a # between 1 - {len(elements)}.")
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
            if order_preference not in ["order", "random", "1", "2", "o", "r"]:
                print(f"{Fore.RED}Enter either 'order' or 'random'")
                continue
            elif order_preference in ["break", exit]:
                break
            break

        element_keys = list(elements.keys())[start_index - 1:]
        if order_preference in ["random", "2", "r"]:
            random.shuffle(element_keys)
        element_keys = element_keys[:num_elements]

        score = 0
        missed_elements = []
        user_answers = {}
        user_inputs = {}
        user_inputs_review = {}
        start_timing = time.time()
        for key in element_keys:
            value = elements[key]
            name = value["name"]
            try:
                user_input_initial = input(f"{Fore.MAGENTA}{name}: ")
                user_input_initial = user_input_initial[0].upper() + user_input_initial[1:]

                result = check_answer(name, user_input_initial, missed_elements, user_answers, user_inputs,
                                      user_inputs_review)
            except IndexError:
                continue

            if result is None:
                print(f"{Fore.RED}No element found with the name {name}.")
            elif not result:
                print(f"{Fore.RED}You got this wrong{Fore.MAGENTA}")
            if user_input_initial.lower() == "break":
                break
            elif result:
                score += 1

            print(f"{Fore.RESET}-------------")

        if score * 100 / num_elements <= 70:
            bold(f"{Fore.RED}Score: {score}/{num_elements}\n")
        elif score * 100 / num_elements >= 80:
            bold(f"{Fore.GREEN}Score: {score}/{num_elements}\n")
        else:
            bold(f"{Fore.RESET}Score: {score}/{num_elements}\n")

        timing(start_timing)
        if score * 100 / num_elements == 100:
            continue
        try_again_or_review = input(
            f"Try again or Review missed questions? ({Fore.GREEN}try/review{Fore.RESET}): ").lower()
        if try_again_or_review in ["try", "try again", "t", "ta"]:
            if missed_elements:
                print_missed_elements(missed_elements, user_answers, user_inputs)
            else:
                print(f"{Fore.GREEN} No missed elements to review.")
                continue
            continue
        elif try_again_or_review in ["review", "review missed", "missed", "question", "2"]:
            for element in missed_elements:
                user_input2 = input(f"{Fore.RESET}{Fore.RED}Correct symbol for {element}: {Fore.RESET}").capitalize()

                if user_input2 == "break":
                    break
                check_answer(element, user_input2, missed_elements, user_answers, user_inputs, user_inputs_review)

            if missed_elements:
                print_missed_elements(missed_elements, user_answers, user_inputs)
            else:
                print(f"{Fore.GREEN} No missed elements to review.")
                continue

        if try_again_or_review.lower() == "break":
            print("Thank you for playing!")

            break
        else:
            continue


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    if elapsed_time < 60:
        time_taken = f"{elapsed_time} seconds"
    else:
        minutes = int(elapsed_time // 60)
        seconds = elapsed_time % 60
        time_taken = f"{minutes} minute(s) and {seconds} seconds"

    print(f"{Fore.RESET}This ran for {time_taken}")
