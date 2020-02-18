#If statement

keep_going = ""
while keep_going == "":

    like_coffee = input("Do you like coffee ? ").lower()

    if like_coffee == "yes" or like_coffee == "y":
        print("I like coffee too")
    elif like_coffee == "no" or like_coffee =="n":
        print("Your missing out")
    else:
        print("I don't understand")

    keep_going = input("Press <enter> to continue or any key to quit")
    print()