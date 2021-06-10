# Imports
import random
import time

# Functions go here

# Checks which questions user would like to answer
def question_checker(question):
    valid = False
    while not valid:

        response = input(question).lower()
        # set list  of the type of questions
        ques_type_list = ["a", "s", "m", "d", ""]

        # Checks how long word is
        if response not in ques_type_list:
            print("<error> please first letter of math question eg: a for addition\n"
            "OR press <eneter> for all types of questions")
            print()
            continue
        else:
            return response


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


# Checks for yes or no responses
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes or no")
            print()


# definition that generates questions randomly and will call this function 
def question(symbol):

    valid = False
    while not valid:
        # Generate random intergers
        int_i = random.randint(1, 100)
        int_ii = random.randint(1, 100)

        ans = eval(str(int_i) + symbol + str(int_ii))
        response = float(input("{} {} {} = ".format(int_i, symbol, int_ii)))

        if response == ans:
            print("You got it right")
            result = "correct"
            print()
            return result
        else:
            print("You got it wrong")
            result = "incorrect"
            print()
            return result


# main routine
play_again = "yes"
while play_again == "yes":

    # reset variables
    questions_answered = 0
    correct_questions = 0
    incorrect_questions = 0
    questions_list = []

    # symbol list
    symbol_list = ["+", "-", "*", "/"]

    # ask user for which type of questions they would like
    question_type = question_checker("Which type of questions would you like? ")
    print()


    # ask uesr for number of questions
    num_questions_error = "<error> enter an interger"
    num_questions = num_check("How many questions? ", num_questions_error, int, 0)
    print()
    
    
    time_set = yes_no("Would you like a timer? ")
    if time_set == "yes":
        # Ask user for the amount of time they get for the questions
        seconds = num_check("how many seconds? ", "enetr an number between 1, 59", int, 0, 60)
        print("Timer set! ")
        print()
        # setting timer
        start = time.time()

        # Generate questions
        while time.time() - start < seconds:

            # generates questions depending on what type you choose
            if question_type == "a":
                result = question("+")
            elif question_type == "s":
                result = question("-")
            elif question_type == "m":
                result = question("x")
            elif question_type == "d":
                result = question("/")
            else:
                result = question(random.choice(symbol_list))

            # Add number of correct and incorrect questions
            if result == "correct":
                correct_questions += 1
            elif result == "incorrect":
                incorrect_questions += 1

            # Add number of questions answered
            questions_answered += 1

            # add question resu;t tpo a list
            questions_list.append("Question #{}: {}".format(result))
            
            # number of questions left go down
            num_questions -= 1

        
    # No timer
    else:
        print("No Timer")

        # Generate questions
        while num_questions > 0:

            # generates questions depending on what type you choose
            if question_type == "a":
                result = question("+")
            elif question_type == "s":
                result = question("-")
            elif question_type == "m":
                result = question("x")
            elif question_type == "d":
                result = question("/")
            else:
                    result = question(random.choice(symbol_list))

            # Add number of correct and incorrect questions
            if result == "correct":
                correct_questions += 1
            elif result == "incorrect":
                incorrect_questions += 1

            # Add number of questions answered
            questions_answered += 1

            # Add question result to a list
            questions_list.append("Question #{}: {}".format(questions_answered + 1, result))
            
            # number of questions left go down
            num_questions -= 1

    # **** Calculate Game Stats ****
    percent_correct = correct_questions / questions_answered * 100
    percent_incorrect = incorrect_questions / questions_answered * 100

    # Displays game stats with % values to the nearest whole number
    print()
    print("**** Quiz Statistics ****")
    print("Win: {}: ({:.0f}%)\nLoss: {}: ({:.0f}%)".format(correct_questions, percent_correct, incorrect_questions, percent_incorrect))
    print()

    # Asks user if they want to see there history
    show_history = yes_no("would you like to see game history? ")

    # displays history if user says yes
    if show_history == "yes":
        print()
        print("**** Quiz History ****")
        for quiz in questions_list:
            print(quiz)

        print()
        print("Thanks for playing")

    # Doesnt display history if user says no
    elif show_history == "no":
        print()
        print("Thanks for Playing")
