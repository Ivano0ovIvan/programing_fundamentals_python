import re


pattern = r'\d+'
data = input()
while data:
    matches = re.findall(pattern, data)
    if matches:
        print(' '.join(matches), end= ' ')
    data = input()