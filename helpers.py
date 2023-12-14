import json
import random

with open("./native_numbers.json", "r") as j:
     native_numbers = json.loads(j.read())

with open("./nouns.json", "r") as j:
     nouns = json.loads(j.read())

with open("./verbs_adjectives.json", "r") as j:
     verbs = json.loads(j.read())


def number_to_native(number: int) -> str:
    number_str = str(number)

    if(number >= 100):
        return "Greater than 100 error";
    
    string = ""
    last_digit = ""

    for i, digit in enumerate(number_str[::-1]):
        if(i == 1 and digit == "2" and last_digit == "0"):
            string = native_numbers["20l"] + string

        elif(i == 0 and int(digit) in [1, 2, 3, 4]):
            string = native_numbers[digit + "l"]

        else:
            string = native_numbers[digit + (i * "0")] + string

        last_digit = digit
        # print(string)

    return string;


def get_verbs(sample = 10) -> list:
    return (random.sample(list(verbs.items()), sample))


def get_nouns(sample = 10) -> list:
    return (random.sample(list(nouns.items()), sample))


if __name__ == "__main__":
    # print(number_to_native(int(input())))
    for word, meaning in get_verbs():
        print(word, meaning)
