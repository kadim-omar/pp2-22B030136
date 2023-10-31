import re

text = "snake_case_string"
pattern = r'_(\w)'

new_text = re.sub(pattern, lambda x: x.group(1).upper(), text)
print(new_text)