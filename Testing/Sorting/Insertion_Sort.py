numbers = [4, 9, 7, 2]

print("Original list:", numbers)


def insertion_sort(numbers):
    for j in range(1, len(numbers)):
        key = numbers[j]
        i = j - 1

        print(f"\nInserting key: {key}")
        print(f"Starting index i: {i}")

        while i >= 0 and numbers[i] > key:
            numbers[i + 1] = numbers[i]
            print(f"After shifting: {numbers}")
            i -= 1

        numbers[i + 1] = key
        print(f"After inserting key: {numbers}")

    return numbers

sorted_numbers = insertion_sort(numbers)

print("\nFinal sorted list:", sorted_numbers)