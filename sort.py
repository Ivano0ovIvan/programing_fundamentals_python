def sorted(current_numbers):
    current_numbers.sort(reverse=False)
    return current_numbers


numbers = input()
numbers_as_int = list(map(int, numbers.split()))
print(sorted(numbers_as_int))