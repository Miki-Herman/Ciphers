cipher = {
    "a":"f",
    "b":"g",
    "c":"h",
    "d":"i",
    "e":"j",
    "f":"k",
    "g":"l",
    "h":"m",
    "i":"n",
    "j":"o",
    "k":"p",
    "l":"q",
    "m":"r",
    "n":"s",
    "o":"t",
    "p":"u",
    "q":"v",
    "r":"w",
    "s":"x",
    "t":"y",
    "u":"z",
    "v":"a",
    "w":"b",
    "x":"c",
    "y":"d",
    "z":"e",
}

plain = input("Please enter a sentence: ")
lower_plain = plain.lower()
words = lower_plain.split()
ceaser =""
for i in range(len(words)):
    char = list(words[i])
    word = ""
    for x in char:
        if x in cipher:
            word += cipher[x]
        else:
            word += x
    
    ceaser += word + " "

print(ceaser)
