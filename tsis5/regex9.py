import re

text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
pattern = r'(?<!^)(?=[A-Z])'

new_text = re.sub(pattern, ' ', text)
print(new_text)