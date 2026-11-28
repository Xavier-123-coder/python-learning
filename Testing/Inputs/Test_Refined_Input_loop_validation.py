def collect_numbers():
    numbers = []
    keep_going = False

    while True:
        choice = input("Type 'Start' to begin entering numbers or 'Exit' to quit:\t").strip().capitalize()

        if choice == "Start":
            keep_going = True
            break

        elif choice == "Exit":
            print("Exiting the program.")
            keep_going = False
            return None

        else:
            print("That isn't a choice. Please type 'Start' or 'Exit'.")
    
    while keep_going:
        try:
            element = int(input("Enter a number:\t"))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        numbers.append(element)

        while True:
            choice = input("Type 'Stop' to finish entering numbers or 'Continue' to enter another:\t").strip().capitalize()

            if choice == "Continue":
                break
    
            elif choice == "Stop":
                keep_going = False
                break

            else:
                print("That isn't a choice. Please type 'Stop' or 'Continue'.")

    return numbers
    
numbers = collect_numbers()

if numbers is None:
    print("Program cancelled.")
else:
    print(numbers)