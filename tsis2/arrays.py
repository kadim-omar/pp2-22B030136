#arrays application
cars = ["Ford", "Volvo", "BMW"]
print(cars)

#length of the array
x = len(cars)

#loops
for x in cars:
  print(x)

#append
cars.append("Honda")

#pop
cars.pop(1)

#remove
cars.remove("Volvo")

'''
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''