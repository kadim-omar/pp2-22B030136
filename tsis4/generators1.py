#1
def square_generator(N):
    for i in range(N):
        yield i**2

# Example usage:
for square in square_generator(5):
    print(square)

#2
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

# Example usage:
n = int(input("Enter a number: "))
even_nums = even_numbers(n)
print(*even_nums, sep=", ")


#3
def div_3_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage:
for num in div_3_4(20):
    print(num)

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

# Example usage:
for square in squares(1, 5):
    print(square)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Example usage:
for num in countdown(5):
    print(num)