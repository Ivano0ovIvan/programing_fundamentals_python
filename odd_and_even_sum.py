def even_and_odd_numbers(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return sum_of_odd_digits, sum_of_even_digits


number_as_string = input()
sum_of_odd_digit, sum_of_even_digits = even_and_odd_numbers(number_as_string)
print(f"Odd sum = {sum_of_odd_digit}, Even sum = {sum_of_even_digits}")