# Lucky Unicorn - end mechanics

# To do
# Ask user how much money they have to play with
# If the total is less than $1, quit
# If the total is more than $1 , ask user if they want to keep going


# Assume starting amount is $10
total = int(input("How much would you like to play with? "))

# Allow manual token input for testing purpose
token = input("enter a token: ")

# Adjust total correctly for a given token
if token == "unicorn":
    total += 5
    feedback = "Congratulation you won $5.00 "
elif token == "donkey":
    total -= 1
    feedback = "Sorry, you did not win anything this round "
else:
    total -= 0.5
    feedback = "Congratulation you won 50c "


print()

print(feedback)
print("You have {} to play with".format(total))
