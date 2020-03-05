# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

import random

# Integer checking function below
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

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money do you want to play with? ", 1, 10)

keep_going  = ""
while keep_going == "":


        # token list includes 10 items to prevent too many unicorns being chosen
        tokens = ["horse", "horse", "horse",
                 "zebra", "zebra", "zebra",
                 "donkey", "donkey", "donkey", "unicorn"]

        # Randomly choose a token from our list above
        token = random.choice(tokens)
        print()
        print("You got a {}".format(token))

        # Adjust total correctly for a given token
        if token == "unicorn":
           balance += 5  # wins $5
           feedback = "Congratulation you won $5.00 "
        elif token == "donkey":
            balance -= 1  # does not win anything (ie: looses $1)
            feedback = "Sorry, you did not win anything this round"
        else:
            balance -= 0.5  # "wins" 50c, paid $1 so loses 50c
            feedback = "Congratulation you won 50c "


        print()
        print(feedback)
        print("You have {} to play with".format(balance))
        print()

        # If user has enough money to play, ask if they want to play again...
        if balance < 1:
            print("Sorry you don't have enough money to continue. Game over")
            keep_going = "end"
        else:
            keep_going = input("Press <enter> to play or any key to quit")


# farewell user at end of game.
print("Thank you for playing")

