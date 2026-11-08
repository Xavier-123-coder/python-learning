numbers = []
keep_going = True

while keep_going:
    element = int(input("Enter a number: "))
    numbers.append(element)

    while True:
        choice = input("Type 'Stop' to finish entering numbers or 'Continue' to enter another:\t").capitalize()

        if choice == "Continue":
            break

        elif choice == "Stop":
            keep_going = False
            break

        else:
            print("That isn't an option. Please type 'Move' or 'Stay'.")

print(f"Your numbers are:\t{numbers}")

target = int(input("What is your target number, lets check if it's in your list!:\t"))

def find(numbers, target):
    if not numbers:
        return False
    
    middle = len(numbers) // 2

    if numbers[middle] == target:
        return True
    
    if numbers[middle] < target:
        return find(numbers[middle + 1:], target)
    
    if numbers[middle] > target:
        return find(numbers[:middle], target)
