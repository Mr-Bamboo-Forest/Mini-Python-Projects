# is a list that contains multiple dictionaries. Each dictionary represents one quiz question
questions = [
    #each one of these is a dictionary, where prompt, options and answer are keys
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "prompt": "Which player scored 5 goals in 9 minutes?",
        "options": ["A. Leo Messi", "B. Cristiano Ronaldo", "C. Robert Lewandowski", "D. No one, that's too difficult"],
        "answer": "C"
    }
]

def run_quiz(questions): # takes questions as the parameter of the function
    score = 0 # makes a score variable and assigns it to 0
    for i in questions: #loop iterates over each question in the questions list, with i representing the current question.
        print(i["prompt"]) #Prints the prompt of the current question
        for option in i["options"]: # Prints each option of the current question, each on a new line
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper() # changes the input into uppercase to ensure any un-capitalised cases are picked up
        if answer == i["answer"]:# Checks if the user's answer matches the correct answer
            print("Correct!\n") #prints correct
            score += 1 #adds one to the score
        else:
            print("Wrong! The correct answer was", i["answer"], "\n") #fixing the users mistake
    print(f"You got {score} out of {len(questions)} questions correct.") #ending which tells the score


# Run the quiz
run_quiz(questions)