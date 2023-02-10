import re

data = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
result = re.findall(pattern, data)
print(','.join(result))