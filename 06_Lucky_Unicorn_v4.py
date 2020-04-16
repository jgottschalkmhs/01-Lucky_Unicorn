# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

import random


# Integer checking function below
def intcheck(question, low, high):
    valid = False
    error = "Whoops! Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# function to print out 'token statement'.
# and bottom of message based on specified character
def token_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# Main routine

# Cost Payout Constants
COST = 1  # cost per round
UNICORN = 5  # unicorn wins $5
ZEB_HOR = 0.5  # zebra- horse "wins" 50c
DONKEY = 0  # donkey does not win anything

# Introduction / Instructions

print("*** Welcome to the Lucky Unicorn Game ****")
print()
print("To play, enter an amount of money between $1 and $10 (whole dollar only).")
print()
print("- It costs $1/round")
print()
print("Payouts...")
print("- Unicorn: ${:.2f}".format(UNICORN))
print("- Horse / Zebra: ${:.2f}".format(ZEB_HOR))
print("- Donkey: ${:.2f}".format(DONKEY))



# Ask user how much they want to play with (min $1, max $25)
balance = intcheck("How much money do you like to play with? $", 1, 25)
round_count = 0

print("**** Game in Progress ****")

keep_going = ""
while keep_going == "":


        # tokens list includes 10 items to prevent too many unicorns being chosen
        tokens = ["horse", "horse", "horse",
                 "zebra", "zebra", "zebra",
                 "donkey", "donkey", "donkey", "unicorn"]

        # Randomly choose a token from our list above
        token = random.choice(tokens)
        round_count += 1

        # Adjust total correctly for a given token
        if token == "unicorn":
            # create and print unicorn statement

            token_statement("***** Congratulation! It's a ${:.2f} {}*****".format(UNICORN, token), "*")
            balance += UNICORN  # wins $5

        elif token == "donkey":
            # print donkey statement
            token_statement("--Sorry. Its a {}. You did not win anything this round--".format(token), "-")
            balance -= COST  # wins nothing (ie: loses $1)

        else:
            # print zebra / horse statement
            token_statement("^^ Good try. Its a {}. You won back 50c ^^".format(token), "^")
            balance -= ZEB_HOR  # wins 50c (ie: paid $1 so loses 50c)

        print()
        print("Rounds Played:  {}  Balance: ${:.2f}" .format(round_count, balance))
        print("You have {} to play with".format(balance))
        print()

        # If user has enough money to play, ask if they want to play again...
        if balance < COST:
            print("Sorry you don't have enough money to continue. Game over")
            keep_going = "end"
        else:
            keep_going = input("Press <enter> to play or any key to quit")


# farewell user at end of game.
print("Thank you for playing")

