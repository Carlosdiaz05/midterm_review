# this won't be part of the midterm

d = {} # empty dict
# left side (english) is key ; right side (spanish) is value
eng_to_spa = {"one": "uno", "two": "dos", "three" : "tres"}
print(eng_to_spa)
print(eng_to_spa["three"])
#print(eng_to_spa["pineapple"]) this will give error as of now

#let's add a new value
eng_to_spa["pineapple"] = "piña"
print(eng_to_spa["pineapple"])
eng_to_spa.update({"yes": "si", "no": "no", "i" : "yo", "am": "soy", "cuban": "cubano"})
print(eng_to_spa)
print(f"i know {len(eng_to_spa)} spanish words")
sentence = "i am cuban"
words = sentence.split()
translation = ""
for word in words:
    translation += eng_to_spa[word]+""
print(f"{sentence} translates to: {translation}")

#in order to check methods type eng_to_spa. and pycharme will give options to autofill
print(list(eng_to_spa.values()))
print(list(eng_to_spa.keys()))
# eng_to_spa.pop("pineapple") we would use this to remove something (key) from the dictionary
#lets remove pineapple
x = eng_to_spa.pop("pineapple")
print(x)
print(eng_to_spa)

#what if we ask for car?
if "car" in eng_to_spa:
    print(eng_to_spa["car"])
else:
    print("i don't know this word")

#alternative to what if we ask for car
print(eng_to_spa.get("car", "Sorry, don't know"))
