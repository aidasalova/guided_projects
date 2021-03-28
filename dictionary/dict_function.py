import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def definition(word): 
    match = get_close_matches(word, data.keys(), n=1, cutoff=0.7)
    if word in data:
        return [f"{index+1}. {element}" for index, element in enumerate(data[word])]
    elif word.title() in data:
        return [f"{index+1}. {element}" for index, element in enumerate(data[word.title()])]
    elif word.upper() in data:
        return [f"{index+1}. {element}" for index, element in enumerate(data[word.upper()])]
    elif match:
        user_input = input(f"Did you mean {match[0]}? Type Y or N: ")
        if user_input == 'Y':
            return [f"{index+1}. {element}" for index, element in enumerate(data[match[0]])]
        elif user_input == 'N':
            return "The word does not exist"
        else:
            return "We didn't understand your entry"
    else:
        return "The word does not exist"

word = input("Type the word: ").lower()

mydefinition = definition(word)

if isinstance(mydefinition, list):
    for item in mydefinition:
        print("\n" + item + "\n")
else:
    print(mydefinition)    
