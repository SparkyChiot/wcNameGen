import random

prefixes = [
    {
        "name": "acorn", 
        "traits": ["nervous", "childish", "insecure", "calm", "careful", "faithful", "loving", "oblivious"],
        "colors": ["brown", "red"]
    },
    {
        "name": "adder",
        "traits": ["troublesome", "fierce", "bloodthirsty", "cold", "daring", "ambitious", "confident", "sneaky", "vengeful", "arrogant", "cunning", "rebellious"],
        "colors": ["any"]
    }, 
    {
        "name": "alder",
        "traits": ["lonesome", "fierce", "cold", "nervous", "righteous", "insecure", "strict", "compassionate", "thoughtful", "ambitious",  
                   "calm", "careful", "faithful", "loving", "loyal", "responsible", "strange", "wise", 
                   "grumpy", "cunning", "oblivious", "gloomy", "sincere", "flamboyant", "rebellious"],
        "colors": ["red", "ginger", "orange", "brown", "lilac", "tortoiseshell"]
    },
    {
        "name": "amber",
        "traits": ["troublesome", "fierce", "childish", "playful", "charismatic", "bold", "nervous", "insecure", "strict", "compassionate", "thoughtful", "confident", "adventurous", 
                   "calm", "loving", "loyal", "responsible", "shameless", "wise", "oblivious", "sincere", "flamboyant"],
        "colors": ["red", "ginger", "orange", "brown", "cream", "yellow", "tortoiseshell"]
    },
    {
        "name": "ant",
        "traits": ["lonesome", "childish", "nervous", "insecure", "compassionate", "thoughtful", "confident", "careful", "faithful", "loyal", 
                   "responsible", "shameless", "strange", "sneaky", "wise", "grumpy", "oblivious", "gloomy", "sincere", "flamboyant", "rebellious"],
        "colors": ["grey", "brown", "black", "tortoiseshell"]
    },
    {
        "name": "apple",
        "traits": ["fierce", "childish", "playful", "charismatic", "bold", "daring", "righteous", "strict", "compassionate", "thoughtful", "ambitious", 
                   "confident", "adventurous", "calm", "careful", "loving", "loyal", "responsible", "strange", "wise", "arrogant", "sincere", "flamboyant"],
        "colors": ["red", "ginger", "orange", "brown", "cream", "yellow", "lilac", "tortoiseshell"]
    },
]

suffixes = [
    {
        "name": "bark",
        "traits": ["fierce", "bloodthirsty", "cold", "charismatic", "bold", "daring", 
                   "righteous", "strict", "thoughtful", "ambitious", "confident", 
                   "loyal", "responsible", "vengeful", "wise", 
                   "arrogant", "competitive", "grumpy", "cunning", "rebellious"],
        "colors": ["any"]
    },   
    {
        "name": "beam",
        "traits": ["childish", "playful", "charismatic", "bold", "daring", 
                   "righteous", "compassionate", "thoughtful", "ambitious", "confident", "adventurous", 
                   "loving", "loyal", "shameless", "strange",
                   "arrogant", "competitive", "sincere", "flamboyant"],
        "colors": ["any"]
    }, 
    {
        "name": "bee",
        "traits": ["troublesome", "childish", "playful", "charismatic", 
                   "righteous", "insecure", "strict", "compassionate", "thoughtful", "ambitious", "confident", "adventurous", 
                   "calm", "careful", "faithful", "loving", "loyal", "responsible", "shameless", "strange", "sneaky", "vengeful", "wise", 
                   "arrogant", "competitive", "grumpy", "cunning", "oblivious", "gloomy", "sincere", "flamboyant", "rebellious"],
        "colors": ["any", "red", "ginger", "orange", "silver", "grey", "blue", "brown", "black", "white", "cream", "yellow", "lilac", "tortoiseshell"]
    },
]



traits = [
    "troublesome", 
    "lonesome", 
    "fierce", 
    "bloodthirsty", 
    "cold", 
    "childish", 
    "playful", 
    "charismatic", 
    "bold", 
    "daring", 
    "nervous", 
    "righteous", 
    "insecure", 
    "strict", 
    "compassionate", 
    "thoughtful", 
    "ambitious", 
    "confident", 
    "adventurous", 
    "calm", 
    "careful", 
    "faithful", 
    "loving", 
    "loyal", 
    "responsible", 
    "shameless", 
    "strange", 
    "sneaky", 
    "vengeful",
    "wise", 
    "arrogant", 
    "competitive", 
    "grumpy", 
    "cunning", 
    "oblivious", 
    "gloomy", 
    "sincere", 
    "flamboyant", 
    "rebellious"
]
colors = [
    "any",
    "red",
    "ginger",
    "orange",
    "silver",
    "grey",
    "blue",
    "brown",
    "black",
    "white",
    "cream",
    "yellow",
    "lilac",
    "tortoiseshell"
]

{
        "name": "",
        "traits": ["troublesome", "lonesome", "fierce", "bloodthirsty", "cold", "childish", "playful", "charismatic", "bold", "daring", 
                   "nervous", "righteous", "insecure", "strict", "compassionate", "thoughtful", "ambitious", "confident", "adventurous", 
                   "calm", "careful", "faithful", "loving", "loyal", "responsible", "shameless", "strange", "sneaky", "vengeful", "wise", 
                   "arrogant", "competitive", "grumpy", "cunning", "oblivious", "gloomy", "sincere", "flamboyant", "rebellious"],
        "colors": ["any", "red", "ginger", "orange", "silver", "grey", "blue", "brown", "black", "white", "cream", "yellow", "lilac", "tortoiseshell"]
    },   

def genRandomTraits():
    pickedTraits = random.sample(traits, 2)
    pickedColor = random.choice(colors)
    return pickedTraits, pickedColor

def getPrefixFromTraits(prefixes, pickedTraits, pickedColor):
    prefixesList = []
    for each in prefixes:
        matches = 0
        for trait in pickedTraits:
            if trait in each["traits"]:
                matches += 1

        if matches == 2 and (pickedColor in each["colors"] or "any" in each["colors"]):
            prefixesList.append(each["name"])

    # Try 1 trait
    if not prefixesList:
        for each in prefixes:
            matches = 0
            for trait in pickedTraits:
                if trait in each["traits"]:
                    matches += 1

            if matches == 1 and (pickedColor in each["colors"] or "any" in each["colors"]):
                prefixesList.append(each["name"])

    # Try 0 traits
    if not prefixesList:
        for each in prefixes:
            if pickedColor in each["colors"] or "any" in each["colors"]:
                prefixesList.append(each["name"])

    return random.choice(prefixesList)

def getSuffixFromTraits(suffixes, pickedTraits, pickedColor):
    suffixesList = []
    for each in suffixes:
        matches = 0
        for trait in pickedTraits:
            if trait in each["traits"]:
                matches += 1

        if matches == 2 and (pickedColor in each["colors"] or "any" in each["colors"]):
            suffixesList.append(each["name"])

    # Try 1 trait
    if not suffixesList:
        for each in suffixes:
            matches = 0
            for trait in pickedTraits:
                if trait in each["traits"]:
                    matches += 1

            if matches == 1 and (pickedColor in each["colors"] or "any" in each["colors"]):
                suffixesList.append(each["name"])

    # Try 0 traits
    if not suffixesList:
        for each in suffixes:
            if pickedColor in each["colors"] or "any" in each["colors"]:
                suffixesList.append(each["name"])

    return random.choice(suffixesList)

def main():
    pickedTraits, pickedColor = genRandomTraits()
    prefix = getPrefixFromTraits(prefixes, pickedTraits, pickedColor)
    suffix = getSuffixFromTraits(suffixes, pickedTraits, pickedColor)
    phrase = prefix + suffix + " is a " + pickedTraits[0] + " and " + pickedTraits[1] + " " + pickedColor + " tom"
    print(phrase)

main()