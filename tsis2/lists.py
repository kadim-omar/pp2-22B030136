thislist = ["apple", "banana", "cherry"]
print(thislist)

#lists allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#len() function
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#also including diiferenet data types in one list
list1 = ["abc", 34, True, 40, "male"]

#type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#list()
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#access items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#check if
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#for loops for a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while loops for a list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#short comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#syntax for comprehension: newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in fruits]

newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]

#sorting lists
#sort alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#sort numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sort descendly
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#customizing sort function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#join several lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

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
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''



