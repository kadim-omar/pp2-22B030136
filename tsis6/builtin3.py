def is_palindrome(s):
    return s == s[::-1]

# Example usage:
string = "racecar"
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")  # Output: racecar is a palindrome