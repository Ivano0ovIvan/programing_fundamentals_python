def group(num, boundary):
    current_group = []
    for current_number in num:
        if current_number <= boundary:
            current_group.append(current_number)
    return current_group


numbers = list(map(int, input().split(', ')))
max_value = 10
group_name = 10
while len(numbers) != 0:
    result = group(numbers, max_value)
    print(f"Group of {group_name}'s: {result}")
    numbers = [num for num in numbers if num not in result]
    max_value += 10
    group_name += 10
