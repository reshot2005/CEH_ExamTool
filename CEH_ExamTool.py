#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import random
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

DEFAULT_NUM_QUESTIONS = 125
PASS_MARK_BASE = 92
VERSION_FILES = {
    "1": ("CEH v13 Practice", "cehv13.json"),
    "2": ("CEH v12 Practice", "cehv12.json"),
}

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"

BANNER = rf"""
{GREEN}     █████████  ██████████ █████   █████    ██████████ █████ █████   █████████   ██████   ██████    ███████████    ███████       ███████    █████      
  ███░░░░░███░░███░░░░░█░░███   ░░███    ░░███░░░░░█░░███ ░░███   ███░░░░░███ ░░██████ ██████    ░█░░░███░░░█  ███░░░░░███   ███░░░░░███ ░░███       
 ███     ░░░  ░███  █ ░  ░███    ░███     ░███  █ ░  ░░███ ███   ░███    ░███  ░███░█████░███    ░   ░███  ░  ███     ░░███ ███     ░░███ ░███       
░███          ░██████    ░███████████     ░██████     ░░█████    ░███████████  ░███░░███ ░███        ░███    ░███      ░███░███      ░███ ░███       
░███          ░███░░█    ░███░░░░░███     ░███░░█      ███░███   ░███░░░░░███  ░███ ░░░  ░███        ░███    ░███      ░███░███      ░███ ░███       
░░███     ███ ░███ ░   █ ░███    ░███     ░███ ░   █  ███ ░░███  ░███    ░███  ░███      ░███        ░███    ░░███     ███ ░░███     ███  ░███      █
 ░░█████████  ██████████ █████   █████    ██████████ █████ █████ █████   █████ █████     █████       █████    ░░░███████░   ░░░███████░   ███████████
  ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░    ░░░░░░░░░░ ░░░░░ ░░░░░ ░░░░░   ░░░░░ ░░░░░     ░░░░░       ░░░░░       ░░░░░░░       ░░░░░░░    ░░░░░░░░░░░ 



{YELLOW}                    CEH EXAM Practice TOOL{RESET}
{CYAN}                 by github.com/reshot2005{RESET}
"""


def animated_banner(text, delay=0.0015):
    """Print banner with typing animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print(Fore.LIGHTBLUE_EX + BANNER + Style.RESET_ALL)


def loading_animation(msg="Loading", loops=10):
    import itertools
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    print(msg + " ", end="")
    for _ in range(loops):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    print("✔️")


def main_menu():
    while True:
        clear()
        banner()
        print(Fore.YELLOW + "Choose CEH Version:" + Style.RESET_ALL)
        for k, (label, _) in VERSION_FILES.items():
            print(f" {k}. {label}")
        choice = input("Select version (1-4) or Q to quit: ").strip()
        if choice.lower() == "q":
            sys.exit(0)
        if choice in VERSION_FILES:
            return VERSION_FILES[choice]


def ask_question_count():
    clear()
    banner()
    raw = input(f"Number of questions (Enter for default {DEFAULT_NUM_QUESTIONS}): ").strip()
    if not raw:
        return DEFAULT_NUM_QUESTIONS
    try:
        val = int(raw)
        if val > 0:
            return val
    except ValueError:
        pass
    print("Invalid number, using default.")
    time.sleep(1)
    return DEFAULT_NUM_QUESTIONS


def load_questions(file_path):
    if not os.path.exists(file_path):
        print(Fore.RED + f"Question file {file_path} not found." + Style.RESET_ALL)
        sys.exit(1)
    with open(file_path, 'r', encoding='utf-8') as f:
        raw = json.load(f)
    questions = []
    for item in raw:
        choices = item.get("choices") or item.get("options")
        questions.append({
            "question": item["question"],
            "choices": choices,
            "answer": [a.upper() for a in item["answer"]]
        })
    return questions


def choose_questions(pool, num):
    return random.sample(pool, min(num, len(pool)))


def ask_question(qn_num, total, question, choices, correct_answer):
    clear()
    banner()
    print(f"{Fore.YELLOW}Question {qn_num} of {total}:{Style.RESET_ALL}\n{question}\n")

    options = list(choices.items())
    random.shuffle(options)
    for i, (key, value) in enumerate(options, start=1):
        print(f"{Fore.CYAN}{i}. {value}{Style.RESET_ALL}")

    while True:
        answer = input("\nYour answer [1-4] (X to exit): ").strip().upper()
        if answer == 'X':
            print("Thanks for playing. Goodbye!")
            sys.exit()
        try:
            idx = int(answer) - 1
            if 0 <= idx < len(options):
                selected_key = options[idx][0]
                if set([selected_key.upper()]) == set(correct_answer):
                    print(Fore.GREEN + "Correct ✅" + Style.RESET_ALL)
                    return True
                else:
                    print(Fore.RED + "Wrong  ❌" + Style.RESET_ALL)
                    print(Fore.YELLOW + f"Correct answer: {', '.join(correct_answer)}" + Style.RESET_ALL)
                    return False
        except ValueError:
            pass
        print(Fore.RED + "Invalid input." + Style.RESET_ALL)



def compute_pass_threshold(num_questions):
    import math
    return int(math.ceil(PASS_MARK_BASE / DEFAULT_NUM_QUESTIONS * num_questions))


def pass_animation():
    frames = ["\\o/", " | ", "/ \\"]
    for _ in range(2):
        for f in frames:
            clear()
            print(Fore.GREEN + "CONGRATULATIONS!" + Style.RESET_ALL)
            print(Fore.YELLOW + f + Style.RESET_ALL)
            time.sleep(0.15)


def encouragement():
    print(Fore.RED + "Don't worry—keep practicing and try again!" + Style.RESET_ALL)


def run_quiz(question_pool, num_questions):
    score = 0
    selected = choose_questions(question_pool, num_questions)
    for i, q in enumerate(selected, 1):
        if ask_question(i, len(selected), q["question"], q["choices"], q["answer"]):
            score += 1
        time.sleep(1)
    percent = (score / len(selected)) * 100
    threshold = compute_pass_threshold(len(selected))
    print(f"\n{Fore.MAGENTA}Score: {score}/{len(selected)} | {percent:.2f}%{Style.RESET_ALL}")
    print(f"Pass mark: {threshold}")
    if score >= threshold:
        pass_animation()
    else:
        encouragement()


def main():
    while True:
        label, filename = main_menu()
        loading_animation("Loading questions")
        questions = load_questions(filename)
        n = ask_question_count()
        run_quiz(questions, n)
        choice = input("\nRetry? (y for retry / m for menu / q to quit): ").strip().lower()
        if choice == 'y':
            continue
        elif choice == 'm':
            continue
        elif choice == 'q':
            break


if __name__ == "__main__":
    main()

