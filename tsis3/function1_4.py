def filter_prime(*numbers):
    for x in numbers:
        if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
            print(x)
        else:
            continue

filter_prime(75,67,29,66)

