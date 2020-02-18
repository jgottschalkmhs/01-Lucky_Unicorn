# Ask the user for a number
# Loop question so that it repeats until valid number is entered
# Make code recyclable!

valid = False
while not valid:
    error = "Whoops! Please enter an integer between 1 and 10"

    try:
        response = int(input("Enter an integer between 1 and 10: "))

        if 1 <= response <= 10:
            valid = True
        else:
            print(error)
            print()

    except ValueError:
           print(error )

print(response)
