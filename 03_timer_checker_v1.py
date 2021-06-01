# functions
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


# Main routine
# looped for tesing
while 1 == 1:
    time_set = yes_no("Would you like a timer? ")
    if time_set == "yes":
        print("Timer set! ")
    else:
        print("No timer. ")
    print()
