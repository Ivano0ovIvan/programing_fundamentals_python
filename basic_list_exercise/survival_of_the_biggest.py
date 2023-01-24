list_of_numbers = input().split()
count_of_numbers_to_remove = int(input())
list_of_numbers_as_digyt = []
for element in list_of_numbers:
    list_of_numbers_as_digyt.append(int(element))
for number in range(count_of_numbers_to_remove):
    list_of_numbers_as_digyt.remove(min(list_of_numbers_as_digyt))
counter = 1
for numbers in list_of_numbers_as_digyt:
    if counter == len(list_of_numbers_as_digyt):
        print(numbers)
    else:
        print(numbers, end=', ')
    counter += 1