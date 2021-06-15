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
def question(symbol, points_val):

    valid = False
    while not valid:

        # Question error if they input unexpected values
        q_error = "Please enter an interger between 0 - 1000 (dont be dumb)"

        # Generate random intergers
        temp_int = random.randint(1, 10)
        int_i = random.randint(1, 10)
        int_ii = temp_int * int_i

        # Get answer and there answer to the question
        ans = eval(str(int_ii) + symbol + str(int_i))
        response = num_check("{} {} {} = ".format(int_ii, symbol, int_i), q_error, int, -1, 1001)

        # check if user got answer correct
        if response == ans:
            statement_generator("You got it right! +{} points".format(points_val), "*", "~")
            result = "correct"
            print()
            return result
        else:
            statement_generator("You got it wrong. -10 points", "|", "-")
            result = "incorrect"
            print()
            return result


# function will print instructions when called
def instructions():
    statement_generator("Instructions", "|", "-")
    print("There are 5 modes you can choose:")
    print()
    print("- Addition, a: 10 points for being correct")
    print("- Subtraction, s: 25 points for being correct")
    print("- Multiplication, m: 50 points for being correct")
    print("- Division, d: 50 points for being correct")
    print("- All, '': 50 points for being correct")
    print()
    print("Try to answer as many questions as possible.")
    print("You can have a timer and see if you can do ")
    print("all the questions in the set time. Every")
    print("incorrect question removes 10 points.")
    return ""


# Gives statements decoration on sides and top
def statement_generator(statement, side_decoration, top_bottom_decoration):

    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# timer function stalls program and counts down
def timer(t):

    print("00 : {}".format(t))

    while t != 0:
        t -= 1
        time.sleep(1)
        print("00 : {}".format(t))


# main routine
statement_generator("Welcome to Rizzos Math Quiz", "!", "=")

# define the saved points 
save_points = 0

# asks if user has played before
# if no print instructions 
played_before = yes_no("Have you played before? ")
if played_before == "no":
    instructions()
print()
print("Enjoy!")

# Main quiz code
play_again = "yes"
while play_again == "yes":

    # reset variables
    questions_answered = 0
    correct_questions = 0
    incorrect_questions = 0
    points = 0
    questions_list = []

    # symbol list
    symbol_list = ["+", "-", "*", "/"]

    # ask user for which type of questions they would like
    question_type = question_checker("Which type of questions would you like? ")

    # ask uesr for number of questions
    num_questions_error = "<error> enter an interger"
    num_questions = num_check("How many questions? ", num_questions_error, int, 0)
    
    # ask user if they want a timer 
    time_set = yes_no("Would you like a timer? ")

    if time_set == "yes":
        # Ask user for the amount of time they get for the questions
        seconds = num_check("how many seconds? ", "enetr an number between 1, 59", int, 0, 60)
        print("Timer set! ")

    # countdown 3, 2, 1, go  uses v1 of timer
    timer(3)

    if time_set == "yes":
        
        print()
        # setting timer
        start = time.time()

        # Generate questions
        while time.time() - start < seconds:

            # generates questions depending on what type you choose
            if question_type == "a":
                result = question("+", 10)
                num_points = 10
            elif question_type == "s":
                result = question("-", 25)
                num_points = 25
            elif question_type == "m":
                result = question("x", 50)
                num_points = 50
            elif question_type == "d":
                result = question("/", 50)
                num_points = 50
            else:
                result = question(random.choice(symbol_list), 50)
                num_points = 50

            # Add number of correct and incorrect questions
            if result == "correct":
                correct_questions += 1
                points += num_points
            elif result == "incorrect":
                incorrect_questions += 1
                points -= 10

            # Add number of questions answered
            questions_answered += 1

            # Add question result to a list
            questions_list.append("Question #{}: {}".format(questions_answered, result))
            
            # number of questions left go down
            num_questions -= 1

        
    # No timer
    else:
        print()

        # Generate questions
        while num_questions > 0:

            # generates questions depending on what type you choose
            if question_type == "a":
                result = question("+", 10)
                num_points = 10
            elif question_type == "s":
                result = question("-", 25)
                num_points = 25
            elif question_type == "m":
                result = question("x", 50)
                num_points = 50
            elif question_type == "d":
                result = question("/", 50)
                num_points = 50
            else:
                result = question(random.choice(symbol_list), 50)
                num_points = 50
            
            # Add number of correct and incorrect questions
            if result == "correct":
                correct_questions += 1
                points += num_points
            elif result == "incorrect":
                incorrect_questions += 1
                points -= 10

            # Add number of questions answered
            questions_answered += 1

            # Add question result to a list
            questions_list.append("Question #{}: {}".format(questions_answered, result))
            
            # number of questions left go down
            num_questions -= 1

    # **** Calculate Game Stats ****
    percent_correct = correct_questions / questions_answered * 100
    percent_incorrect = incorrect_questions / questions_answered * 100

    # Displays game stats with % values to the nearest whole number
    print()
    statement_generator("Quiz Statistics", "-", "*")
    print("Correct: {}: ({:.0f}%)\nIncorrect: {}: ({:.0f}%)".format(correct_questions, percent_correct, incorrect_questions, percent_incorrect))
    print()

    # Print and figure out new high score 
    if points > save_points:
        print("NEW HIGH SCORE")
    else:
        print("Nice Job!")
    print("Total points: ", points)
    print()


    # Asks user if they want to see there history
    show_history = yes_no("would you like to see game history? ")

    # displays history if user says yes
    if show_history == "yes":
        print()
        statement_generator("Quiz History", "-", "*")
        for quiz in questions_list:
            print(quiz)

        print()
        statement_generator("Thanks for playing", "!", "=")

    # Doesnt display history if user says no
    elif show_history == "no":
        print()
        statement_generator("Thanks for playing", "!", "=")
    
    # Ask user if they want to play again
    print()
    play_again = yes_no("Would you like to play again? ")
    if play_again == "yes":
        print()
        continue
    else:
        play_again = "no"
