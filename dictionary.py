import json
from difflib import get_close_matches

data = json.load(open("/Users/faitusjelinejoseph/Documents/Python_Programs/Excercise1/data.json"))

print(type(data))
    

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
         yn = input("Did you mean %s instead? if Yes press Y or N if no: " % get_close_matches(w,data.keys())[0])
         if yn == "Y":
             return data[get_close_matches(w,data.keys())[0]]
         elif yn == "N":
             print("Word does not exist! Please double check..")
         else:
             print("We didnt upderstand your entry..")
    else:
        print("Word does not exist! Please double check..")


word = input("Enter a word: ")
output = translate(word)

if type(output) == list:
    print(type(output))
    for item in output:
        print(item)
else:
    print(type(output))
    print(output)
        
