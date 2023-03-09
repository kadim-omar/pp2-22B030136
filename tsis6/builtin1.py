from functools import reduce

def multiply_list(lst):
    product = reduce((lambda x, y: x * y), lst)
    return product

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print(result)  # Output: 120