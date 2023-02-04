number = input().split(' ')
rounded_numbers = []
for num in number:
    rounded_numbers.append(round(float(num)))
print(rounded_numbers)