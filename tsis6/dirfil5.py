my_list = ["apple", "banana", "cherry"]

with open("file.txt", "w") as file:
    for item in my_list:
        file.write("%s\n" % item)