def find_smallest_largest(numbers):
    smallest = min(numbers)
    largest = max(numbers)

    return smallest, largest
numbers = [4, 7, 2, 9, 1, 5]
smallest, largest = find_smallest_largest(numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)
