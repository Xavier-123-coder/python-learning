numbers = []

def number():
    for i in range(1,7,1):
        element = int(input(f"What would you like your number {i} to be (it must be in acsending order!):\t"))
        numbers.append(element)

number()

target = int(input("What is the target number you want to find in your list:\t"))

def find(numbers, target):
    if not numbers:
        return f"{target} is not in your list"
        
    middle = len(numbers) // 2
    
    if numbers[middle] == target:
        return f"{target} was found in your list"
    
    if numbers[middle] < target:
        return find(numbers[middle + 1:], target)
        
    if numbers[middle] > target:
        return find(numbers[:middle], target)


print(find(numbers, target))