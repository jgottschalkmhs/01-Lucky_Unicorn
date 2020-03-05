# Function to easily generate winning statements ....

def token_staement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

# Main routine

COST = 1    # cost per round
UNICORN = 5  # unicorn wins $5
ZEB_HOR = 0.5  # zebra- horse "wins" 50c
DONKEY = 0   # donkey does not win anything

token = [" unicorn", "horse", "donkey", "zebra"]

for token in token:

    if token == "unicorn":
        token_staement("***** Congratulation! It's a ${:.2f} {}*****" .format(UNICORN, token), "*")
    elif token == "donkey":
        token_staement("--Sorry. Its a {}. You did not win anything this round--".format(token), "-")
    else:
        token_staement("^^ Good try. Its a {}. You won back 50c ^^".format(token), "^")


