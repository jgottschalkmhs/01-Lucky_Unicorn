# Lucky Unicorn - payment mechanics

# To do
# Assume starting amount is $10
# Allow manual token input for testing purpose
# Adjust total correctly for a given token
# - if its unicorn add $5
# - if it's a zebra / horse, subtract 0.5
# - if it's donkey, subtract 1
# Give users feedback based on winnings ..
# state the total

# Assume starting amount is $10
total = 10

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
