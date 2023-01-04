abc = "abcdefghijklmnopqrstuvwxyz"
shift = input("Please enter the number of places to shift: ")

if shift.isdecimal() == True and int(shift) <= 25 and int(shift) >= 0:
    plain = input("Please enter a sentence: ")
    lower_plain = plain.lower()
    shifted_abc = abc[int(shift):] + abc[:int(shift)]
    words = lower_plain.split()
    ciper = ""
    for i in range(len(words)):
        char = list(words[i])
        word = ""
        for x in char:
            if x in abc:
                char_index = abc.find(x)
                word += shifted_abc[char_index]
            else:
                word += x

        ciper += word + " "

    print(ciper)

else:
    print("You need to enter a number between 0 and 25!")