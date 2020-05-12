import random


theasures={"hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
"cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
"happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
"sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']}

for key in theasures.keys():
    print(key)
user_input=input("what word they would like to get a synonym:")
if user_input in theasures.keys():
    index=random.randint(0,4)
    print("The synonym for "+user_input+" is "+theasures[user_input][index])
else:
    print("no such word")
user_input=input("would you like to see whole theasures:Y/N").title()
if user_input=="Y":
    for keys,values in theasures.items():
        print("the synonyms are:"+keys)
        for value in values:
            print(value)
else:
    print("program finished")