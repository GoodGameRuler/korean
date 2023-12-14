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
    while(mode := (input("Choose mode (1. Nouns, 2. Polite Forms, 3. Grammar, 4 Native Korean Numbers, 5 Time of Day, 6 Counters): "))):

        mode = int(mode)
    
        if(mode == 1):

            score: int = 0
            no_questions: int = len(nouns)

            for word, meaning in randomised_nouns:
                answer = input(f"What is the koren word for {meaning}?\n")

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
                answer = input(f"What is the korean number for {number}?\n")

                if(normalize_korean_string(answer) == normalize_korean_string(helpers.number_to_native(number))):
                    print("Correct\n")
                    score += 1

                else:
                    print(f"Wrong answer - {answer} - correct ans - {helpers.number_to_native(number)}\n")

            print(f"Your score was {score}/{no_questions}")

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
