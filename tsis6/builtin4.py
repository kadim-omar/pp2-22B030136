import time
import math

def square_root_with_delay(num, delay):
    time.sleep(delay / 1000)
    result = math.sqrt(num)
    return result

# Example usage:
number = 25100
delay = 2123
result = square_root_with_delay(number, delay)
print("Square root of", number, "after", delay, "milliseconds is", result)
# Output: Square root of 25100 after 2123 milliseconds is 158.42979517754858