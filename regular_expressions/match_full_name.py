import re

text = input()
search_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
results = re.findall(search_pattern, text)
print(' '.join(results))