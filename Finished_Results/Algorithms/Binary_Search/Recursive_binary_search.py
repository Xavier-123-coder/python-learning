numbers = [3, 8, 12, 17, 24, 31, 42, 56, 71]

def find_number(numbers, target):
    if not numbers:
        return False
    
    middle = len(numbers)// 2

    if numbers[middle] == target:
        return True
    
    if numbers[middle] < target:
        return find_number(numbers[middle + 1:], target)

    if numbers[middle] > target:
        return find_number(numbers[:middle], target)


print(find_number(numbers, 42))