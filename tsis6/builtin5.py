def all_true(t):
    return all(t)

# Example usage:
t1 = (True, True, False)
t2 = (1, "hello", [1, 2, 3])
t3 = (True, 1, [1, 2, 3])
print(all_true(t1))  # Output: False
print(all_true(t2))  # Output: True
print(all_true(t3))  # Output: True