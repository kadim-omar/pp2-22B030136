import re

text = "ab"
pattern = r'a(b*)'

match = re.match(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")