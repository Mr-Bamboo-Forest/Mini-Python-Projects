import string
from time import sleep

def cool():
    target = "Hello World!"
    result = "" 

    for char in target:
        for letter in string.printable: 
            current_guess = result + letter
            print(current_guess)
            sleep(0.005)

            if letter == char:
                result += letter
                break  
cool()
