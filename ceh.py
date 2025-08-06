import json
import os
import random
import sys
import time
from colorama import Fore, Style, init

init()

def internet_check():
    import requests
    try:
        requests.get("http://www.google.com", timeout=5)
    except requests.RequestException:
        print(f"{Fore.RED}No internet connection. Please check your connection.{Style.RESET_ALL}")
        sys.exit(1)

def banner():
    ascii_art = r"""
   ____  _       _      ____        _         _  __       
  / __ \(_)     | |    |  _ \      (_)       | |/ /       
 | |  | |_  __ _| |__  | |_) |_   _ _ _ __   | ' / ___ _ __
 | |  | | |/ _` | '_ \ |  _ <| | | | | '_ \  |  < / _ \ '__|
 | |__| | | (_| | | | || |_) | |_| | | | | | | . \  __/ |   
  \____/|_|\__, |_| |_|____/ \__,_|_|_| |_| |_|\_\___|_|   
             __/ |                                         
            |___/   Cyber Quiz v1.5 by YOU | H3LLKY4T Style
────────────────────────────────────────────────────────────
    Based on CEH v12 | Customized JSON | Local Questions   
────────────────────────────────────────────────────────────
"""
    print(Fore.LIGHTBLUE_EX + ascii_art + Style.RESET_ALL)

def load_question_bank(filename='ceh_questions.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"{Fore.RED}Failed to load question bank: {e}{Style.RESET_ALL}")
        sys.exit(1)

def loading_animation():
    import itertools
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    print("Loading Quiz Engine ", end="")
    for _ in range(10):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    print("✔️")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_question(qn_num, question, choices, correct_answer):
    clear()
    banner()
    print(f"{Fore.YELLOW}Question {qn_num}:{Style.RESET_ALL}\n{question}\n")

    options = list(choices.items())
    random.shuffle(options)

    for i, (key, value) in enumerate(options, start=1):
        print(f"{Fore.CYAN}{i}. {value}{Style.RESET_ALL}")

    while True:
        try:
            answer = input("\nYour answer [1-4] (X to exit): ").strip().upper()
            if answer == 'X':
                print("Thanks for playing. Goodbye!")
                sys.exit()
            choice_index = int(answer) - 1
            if 0 <= choice_index < len(options):
                selected_key = list(choices.keys())[list(choices.values()).index(options[choice_index][1])]
                if selected_key in correct_answer:
                    print(f"{Fore.GREEN}✅ Correct!{Style.RESET_ALL}")
                    return True
                else:
                    correct_option = next(v for k, v in choices.items() if k in correct_answer)
                    print(f"{Fore.RED}❌ Wrong. Correct Answer: {correct_option}{Style.RESET_ALL}")
                    return False
            else:
                raise ValueError
        except (ValueError, IndexError):
            print(f"{Fore.RED}Invalid input. Please enter a number from 1 to 4 or 'X' to exit.{Style.RESET_ALL}")

def choose_questions(pool, num):
    return random.sample(pool, min(num, len(pool)))

def get_user_question_count():
    clear()
    banner()
    while True:
        choice = input("Do you want to set the number of questions? (yes/no): ").strip().lower()
        if choice == 'yes':
            try:
                return int(input("Enter number of questions: ").strip())
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 'no':
            return 125
        else:
            print("Please enter 'yes' or 'no'.")

def run_quiz(question_pool, num_questions):
    score = 0
    selected = choose_questions(question_pool, num_questions)
    for i, q in enumerate(selected, 1):
        correct = ask_question(i, q["question"], q["choices"], q["answer"])
        if correct:
            score += 1
        time.sleep(2)
    percent = (score / len(selected)) * 100
    print(f"\n{Fore.LIGHTMAGENTA_EX}🎉 Quiz Finished! Score: {score}/{len(selected)} | {percent:.2f}%{Style.RESET_ALL}")
    print("Press Ctrl + C to exit")

def main():
    internet_check()  # Optional - can be commented out for offline use
    loading_animation()
    question_pool = load_question_bank()
    question_count = get_user_question_count()
    run_quiz(question_pool, question_count)

if __name__ == "__main__":
    main()
