import random
import string

#Password Creator


def createPassword(length):
    count = 0
    pWord = "" 

    while count < length:
        choice = random.randint(0, 1)
        if choice == 0:
            pWord += random.choice(string.ascii_letters)
        else:
            pWord += str(random.randint(0,9))
        
        count += 1

    return pWord

inp = input("Enter a number: ")

try:
    inp = int(inp)
except:
    print("ERROR, please enter a number!!!")
    quit()

print("This is your random password:", createPassword(inp))