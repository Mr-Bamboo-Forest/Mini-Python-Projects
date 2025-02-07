import string
from time import sleep

def cool():
    target = "Hello World!"
    result = "" 

    for char in target:
        for letter in (string.ascii_letters + " !"): 
            current_guess = result + letter
            print(current_guess)
            sleep(0.03)

            if letter == char:
                result += letter
                break  

cool()
