x="amazing"
def my_func():
    print("Python is" + x)

my_func()

x="incredible"
def my_func():
    x="amazing"
    print("Python is"+x)
print("Python is"+x)

def my_func():
    global x
    x="outstanding"
my_func()
print("Python is"+x)

x="incredible"
def my_func():
    global x
    x="outstanding"
my_func()
print("Python is"+x)
