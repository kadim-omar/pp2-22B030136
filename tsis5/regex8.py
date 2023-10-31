import re

text = "SplitThisStringAtUpperCaseLetters"
pattern = r'[A-Z]'

result = re.split(pattern, text)
print(result)