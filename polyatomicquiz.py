import sys
from prettytable import PrettyTable
import random
import time
from chemical import polyatomic
from functions import *
batman()
def bold(tpas):
    sys.stdout.write("\033[1m" + tpas + "\033[0m")


def check_answer(name, symbol, missed_elements, user_answers, user_inputs, user_inputs_review, direction):
    for key, value in polyatomic.items():
        if direction == "name_to_polyatomic":
            if value.lower() == name.lower() and key.lower() == symbol.strip().lower():
                return True
        elif direction == "polyatomic_to_name":
            if key.lower() == name.strip().lower() and value.lower() == symbol.strip().lower():
                return True

        if direction == "name_to_polyatomic" and value.lower() == name.lower() and key.lower() != symbol.strip().lower():
            missed_elements.append(name)
            user_answers[name] = key
            user_inputs[name] = symbol
            user_inputs_review[name] = [key, symbol]
            return False
        elif direction == "polyatomic_to_name" and key.lower() == name.strip().lower() and value.lower() != symbol.strip().lower():
            missed_elements.append(name)
            user_answers[name] = value
            user_inputs[name] = symbol
            user_inputs_review[name] = [value, symbol]
            return False
        elif direction == "name_to_polyatomic" and value.lower() == name.lower() and key.lower() == symbol.strip().lower():
            return True
        elif direction == "polyatomic_to_name" and key.lower() == name.strip().lower() and value.lower() == symbol.strip().lower():
            return True

    return None

# Rest of the code remains the same...



def print_missed_elements(missed_elements, user_answers, user_inputs):
    table = PrettyTable()
    table.field_names = [f"Polyatomic Ion", f"Correct", f"Your answer"]
    table.title = "Missed polyatomic ions"
    for element in missed_elements:
        table.add_row([element, user_answers[element], user_inputs[element]])
    print(table)

def main():
    order_preference = input("In order or randomized: ").lower()
    if order_preference not in ["order", "random", "1", "2", "o", "r"]:
        print("Enter either 'order' or 'random'")
        return

    matching_direction = input("Match from polyatomic to name or name to polyatomic (1/2): ")
    if matching_direction == "1":
        direction = "polyatomic_to_name"
    elif matching_direction == "2":
        direction = "name_to_polyatomic"
    else:
        print("Invalid input. Please enter '1' or '2'.")
        return

    element_keys = list(polyatomic.keys())
    if order_preference in ["random", "2", "r"]:
        random.shuffle(element_keys)

    score = 0
    missed_elements = []
    user_answers = {}
    user_inputs = {}
    user_inputs_review = {}
    start_timing = time.time()

    for key in element_keys:
        value = polyatomic[key]
        if direction == "name_to_polyatomic":
            name = value
        elif direction == "polyatomic_to_name":
            name = key

        try:
            user_input_initial = input("{}: ".format(name))
            user_input_initial = user_input_initial[0].upper() + user_input_initial[1:]

            result = check_answer(name, user_input_initial, missed_elements, user_answers, user_inputs,
                                  user_inputs_review, direction)
        except IndexError:
            continue

        if result is None:
            print("No polyatomic ion found with the name {}.".format(name))
        elif not result:
            print("You got this wrong")
        if user_input_initial.lower() == "break":
            break
        elif result:
            score += 1

        print("-------------")

    if score * 100 / len(element_keys) <= 70:
        bold("Score: {}/{}\n".format(score, len(element_keys)))
    elif score * 100 / len(element_keys) >= 80:
        bold("Score: {}/{}\n".format(score, len(element_keys)))
    else:
        bold("Score: {}/{}\n".format(score, len(element_keys)))

    elapsed_time = time.time() - start_timing
    if score * 100 / len(element_keys) == 100:
        return

    try_again_or_review = input("Try again or Review missed questions? (try/review): ").lower()
    if try_again_or_review in ["try", "try again", "t", "ta"]:
        if missed_elements:
            print_missed_elements(missed_elements, user_answers, user_inputs)
        else:
            print("No missed polyatomic ions to review.")
            return
    elif try_again_or_review in ["review", "review missed", "missed", "question", "2"]:
        for element in missed_elements:
            user_input2 = input("Correct symbol for {}: ".format(element)).capitalize()

            if user_input2 == "break":
                break
            check_answer(element, user_input2, missed_elements, user_answers, user_inputs, user_inputs_review,
                         direction)

        if missed_elements:
            print_missed_elements(missed_elements, user_answers, user_inputs)
        else:
            print("No missed polyatomic ions to review.")
            return

    if try_again_or_review.lower() == "break":
        print("Thank you for playing!")
        return
    else:
        return


if __name__ == "__main__":
    main()
