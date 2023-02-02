def filter(current_numbers):
    list_of_even_numbers = []
    for number in current_numbers:
        if int(number) % 2 == 0:
            list_of_even_numbers.append(int(number))
    return list_of_even_numbers


numbers = input()
numbers = list(map(int, numbers.split()))
print(filter(numbers))
