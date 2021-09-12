import json
from difflib import get_close_matches

data =json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
        #this code is for close matches realted to search
    elif len(get_close_matches(word , data.keys())) > 0: # in this line of code 0 the
        print("did you mean this %s" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no\n")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return ("you made a typo")
        else:
            return ("You entered a wrong word...just to clarification press y or no")
    else:
        print("you made a typo")

word = input("Enter the the particular word you want to know ")
output = translate(word)
#the code helps to seperate line of a word which have more then one meaning
if type(output) == list:
    for item in output:
    print(item)
else:
    print(output)
