maded_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0
for snowballs in range(maded_snowballs):
    snowball_weight = int(input())
    time_needed = int(input())
    snowball_quality = int(input())
    current_snowball_value = (snowball_weight / time_needed) ** snowball_quality
    if current_snowball_value > max_value:
        max_weight = snowball_weight
        max_time = time_needed
        max_quality = snowball_quality
        max_value = int(current_snowball_value)
print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")