import re

text = "abbb"
pattern = r'a(b{2,3})'

match = re.match(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")