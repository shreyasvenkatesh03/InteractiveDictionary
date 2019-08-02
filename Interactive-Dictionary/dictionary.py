import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):

    word = word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s ? Enter Y is yes, else N : " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The word entered doesnt exist, try again!"
        else:
            return "Entered query is invalid!"
    else:
        return "The word entered doesnt exist, try again!"

word = input("Enter the word : ")

output = definition(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
