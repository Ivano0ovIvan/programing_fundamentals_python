import re

data = input()
pattern_for_emojis = r'([\:]{2}|[\*]{2})([A-Z][]a-z]{2,})(\1)'
matches_for_emojis = re.findall(pattern_for_emojis, data)
count_of_valid_emojis = len(matches_for_emojis)
pattern_for_digits = r'([0-9])'
matches_for_digits = re.findall(pattern_for_digits, data)
cool_threshold = 1
for x in matches_for_digits:
    cool_threshold = cool_threshold * int(x)
print(f"Cool threshold: {cool_threshold}")
print(f"{count_of_valid_emojis} emojis found in the text. The cool ones are:")
index = 0
cool_emojis = []
current_sum = 0
for emoji in matches_for_emojis:
    current_emoji = matches_for_emojis[index][1]
    for ch in current_emoji:
        current_sum += ord(ch)
    if current_sum > cool_threshold:
        cool_emojis.append(''.join(matches_for_emojis[index]))
    current_sum = 0
    index += 1
for emojis in cool_emojis:
    print(emojis)
