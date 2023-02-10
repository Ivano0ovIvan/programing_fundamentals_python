first_str, second_str = input().split()
total_sum = 0
if len(first_str) > len(second_str):
    for index in range(len(second_str)):
        total_sum += ord(first_str[index]) * ord(second_str[index])
    for index in range(len(second_str), len(first_str)):
        total_sum += ord(first_str[index])

elif len(second_str) > len(first_str):
    for index in range(len(first_str)):
        total_sum += ord(first_str[index]) * ord(second_str[index])
    for index in range(len(first_str), len(second_str)):
        total_sum += ord(second_str[index])

elif len(first_str) == len(second_str):
    for index in range(len(first_str)):
        total_sum += ord(first_str[index]) * ord(second_str[index])

print(total_sum)