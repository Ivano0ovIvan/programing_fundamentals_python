def calculator(number_a, number_b, operator):
    if operator == "multiply":
        return number_a * number_b
    elif operator == "divide":
        return int(number_a / number_b)
    elif operator == "add":
        return number_a + number_b
    elif operator == "subtract":
        return number_a - number_b

type_of_operator = input()
first_number = int(input())
second_number = int(input())
print(calculator(first_number, second_number, type_of_operator))
