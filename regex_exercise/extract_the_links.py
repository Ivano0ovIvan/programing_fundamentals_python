import re

valid_urls = []
pattern = r'(www\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
data = input()
while data:
    matches = re.search(pattern, data)
    if matches:
        valid_urls.append(matches.group(0))
    data = input()
for valid_url in valid_urls:
    print(valid_url)