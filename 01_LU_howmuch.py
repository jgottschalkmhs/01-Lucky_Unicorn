# Component 1: Ask user how much money
# Check that amount is an integer that is more / than equal to 1 and less than /


# Number checking function goes here
def intcheck(question, low, high):
    valid = False
    error = "Whoops! Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input("Enter an integer between {} and {}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# main routine goes here

how_much = intcheck("How much money do you want to play with? ", 1, 10)