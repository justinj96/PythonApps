#program tells you the definition of a word by reading data.json

import json
from difflib import get_close_matches

data = json.load(open("data.json")) 

def main():
    word = input("Enter a word: ").lower()

    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    restart = input("Would you like to look up another word? Y or N: ").lower()

    if (restart == "y"):
        main()

def translate(word):

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Y if yes, N if no: " % get_close_matches(word, data.keys())[0]).lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "Word does not exist"
        else:
            return "Did not understand query"
    else:
        return "Invalid entry, please try again"

main()   