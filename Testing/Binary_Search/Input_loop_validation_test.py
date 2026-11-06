numbers = []

while keep_going:
    element = int(input("Enter a number: "))
    numbers.append(element)

    while True:
        choice = input("Type 'Move' to finish entering numbers or 'Stay' to enter another:\t").capitalize()

        if choice == "Continue":
            break

        elif choice == "Stop":
            keep_going = False
            break

        else:
            print("That isn't an option. Please type 'Move' or 'Stay'.")