import re

text = "Hello, world. How are you?"
pattern = r'[ ,\.]+'

new_text = re.sub(pattern, ':', text)
print(new_text)