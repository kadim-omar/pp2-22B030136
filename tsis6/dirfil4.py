with open("file.txt", "r") as file:
    line_count = sum(1 for line in file)

print("Number of lines in the file:", line_count)