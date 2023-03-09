def count_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

# Example usage:
string = "Hello, World!"
upper, lower = count_letters(string)
print("Number of uppercase letters:", upper)  # Output: 2
print("Number of lowercase letters:", lower)  # Output: 10