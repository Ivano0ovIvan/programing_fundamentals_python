import re


data = input()
pattern = r'([\|\#])([A-Za-z\s?]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1'
matches = re.findall(pattern, data)
index = 0
index1 = 0
total_calories = 0
for match in range(len(matches)):
    total_calories += int(matches[index1][3])
    index1 += 1
days_left = total_calories // 2000
print(f"You have food to last you for: {days_left} days!")
for match in range(len(matches)):
    item_name, expiration_date, calories = matches[index][1], matches[index][2], int(matches[index][3])
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
    index += 1
