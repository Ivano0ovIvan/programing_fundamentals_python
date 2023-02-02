def sum_numbers(number_1, number_2):
        return number_1 + number_2


def subtract(sum, number_3):
        return sum - number_3


def add_and_subtract(number_1, number_2, number_3):
    sum_of_number_1_and_number_2 = sum_numbers(number_1, number_2)
    result = subtract(sum_of_number_1_and_number_2, number_3)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))