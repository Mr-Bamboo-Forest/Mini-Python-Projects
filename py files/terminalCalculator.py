import math
# General
def general():
    math_question = input("Enter a math question (2+1, 10/2, 3-2, 3*5):")
    try:
        result = eval(math_question)
        print(result)
    except:
        print("Invalid input, please try again.")

#logs
def log():
    user_input_base = input("Enter base of log: ")
    user_input_log = input("Enter x of log: ")
    try:
        log_int = int(user_input_log)
        log_int_2 = int(user_input_base)
        log_answer = math.log(log_int, log_int_2) 
        print(round(log_answer,10))
        print("Numbers are rounded to 5 decimal places.")
    except:
        print("Invalid input, please try again.")

#cosine
def cos():
    user_cosine_input1 = input('Enter cosine: ')
    try:
        user_cosine_input = int(user_cosine_input1)
        user_cosine_solve = math.cos(user_cosine_input)
        print(user_cosine_solve)
    except: 
        print('Invalid input, please try again.')

#sine
def sin():
    user_sine_input1 = input('Enter sine: ')
    try:
        user_sine_input = int(user_sine_input1)
        user_sine_solve = math.sin(user_sine_input)
        print(user_sine_solve)
    except: 
        print('Invalid input, please try again.')

#tangent
def tan(): 
    user_tan_input1 = input('Enter tan value: ')
    try: 
        user_tan_input = int(user_tan_input1)
        user_tan_solve = math.tan(user_tan_input)
        print(user_tan_solve)
    except:
        print('Invalid input, please try again.')  

#factorial
def factorial():
    user_input_tan = input('Enter a factorial value: ')
    try: 
        user_factorial_number = int(user_input_tan)
        user_factorial_solve = math.factorial(user_factorial_number)
        print(user_factorial_solve)
    except: 
        print('Invalid input, please try again.')

#calculator
def calculator():
    while True:
        user_input = input("Enter a type of maths (general, log, cos, sin, tan, factorial) or type exit to exit: ")
        #exit
        if user_input == 'exit':
            break
        #pi
        if user_input == 'pi':
            print(math.pi)
        #e 
        if user_input == 'e':
            print(math.e)
        #general
        if user_input == 'general' or user_input == 'g':
            general()
        #logarithms
        if user_input == 'log' or user_input == 'l':
            log()
        #cosine
        if user_input == 'cos' or user_input == 'c':
            cos()
        #sine
        if user_input == 'sin' or user_input == 's':
            sin()
        #tangent
        if user_input == 'tan' or user_input == 't': 
            tan()  
        #factorial 
        if user_input == 'factorial' or user_input == 'f':
            factorial()
calculator()
