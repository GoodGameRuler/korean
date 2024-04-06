#!/bin/python3.12

import unicodedata
import random
import signal
import json

def quit_gracefully(num, frame):
    print("\nQuitting gracefully!")
    exit(0)


signal.signal(signal.SIGINT, quit_gracefully)

import helpers

with open("./nouns.json", "r") as j:
     nouns = json.loads(j.read())

randomised_nouns = list(nouns.items())
random.shuffle(randomised_nouns)

def normalize_korean_string(korean_string: str) -> str:
    # Normalize the string using NFC (Normalization Form Canonical Composition)
    return unicodedata.normalize('NFC', korean_string).strip()


def main():
    while(mode := (input("Choose mode (1. Nouns, 2. Verbs and Adjectives, 3. Grammar, 4 Native Korean Numbers, 5 Time of Day, 6 Counters, 7. Polite Forms, ): "))):

        mode = int(mode)

        if(mode == 1):

            score: int = 0
            no_questions: int = 10

            for word, meaning in helpers.get_nouns(no_questions):
                answer = input(f"What is the koren word for `{meaning}`?\n")

                if(normalize_korean_string(answer) == normalize_korean_string(word)):
                    print("Correct\n")
                    score += 1

                else:
                    print(f"Wrong answer - {word}\n")

            print(f"Your score was {score}/{no_questions}")

        if(mode == 2):

            score: int = 0
            no_questions: int = 10

            for word, meaning in helpers.get_verbs(no_questions):
                answer = input(f"What is the koren word for `{meaning}`?\n")

                if(normalize_korean_string(answer) == normalize_korean_string(word)):
                    print("Correct\n")
                    score += 1

                else:
                    print(f"Wrong answer - {word}\n")

            print(f"Your score was {score}/{no_questions}")

        elif(mode == 4):

            score: int = 0
            no_questions: int = 5

            for number in random.sample(range(1, 100), 5):
                answer = input(f"What is the korean number for `{number}`?\n")

                if(normalize_korean_string(answer) == normalize_korean_string(helpers.number_to_native(number))):
                    print("Correct\n")
                    score += 1

                else:
                    print(f"Wrong answer - {answer} - correct ans - {helpers.number_to_native(number)}\n")

            print(f"Your score was {score}/{no_questions}")

        elif(mode == 6):

            hour = "시"
            minutes = "분"

            am_pm = ["오후", ""]

            score: int = 0
            no_questions: int = 4

            for _ in range(10):
                hours = (random.randint(1,12))
                minutes = (random.randint(0,60))
                am = (random.randint(1, 2))
                answer = input(f"What is the korean expression for {hours}:{minutes} {'am' if am == 1 else 'pm'}?\n")

                if(normalize_korean_string(answer) == am_pm[am] + " " +  normalize_korean_string(helpers.number_to_native(hours)) + ":" + str(minutes)):
                    print("Correct\n")
                    score += 1

                # else:
                #     print(f"Wrong answer - {answer} - correct ans - {am_pm[am] + " " +  normalize_korean_string(helpers.number_to_native(hours)) + ":" + str(minutes)} \n")

        elif(mode == 6):

            counters = {"animals": "마리", "people": "명", "items": "게", "lessons": "과"}

            score: int = 0
            no_questions: int = 4

            for meaning, counter in counters.items():
                number = (random.randint(1,10))
                answer = input(f"What is the korean expression for {number} {meaning}?\n")

                if(normalize_korean_string(answer) == normalize_korean_string(helpers.number_to_native(number) + counter)):
                    print("Correct\n")
                    score += 1

                else:
                    print(f"Wrong answer - {answer} - correct ans - {helpers.number_to_native(number)}{counter}\n")

            print(f"Your score was {score}/{no_questions}")


if __name__ == "__main__":
    main()
