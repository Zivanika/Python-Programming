f = open("temp.txt", "w")
f.write("Tandoori Butter")
f.close()  # Mandatory to close the file after writing otherwise changes does not gets saved

f = open("temp.txt", "r")
print(f.read())

with open("temp.txt", "a") as f:
    f.write(" I Eat")
# No need to close file

# Reading marks of students in three subjects
f = open("marks.txt", "r")
i = 1
while True:
    j = 1
    line = f.readline()
    # print(line)
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in subject {j} is {m1*2}")  # This m1 is a string
    j += 1
    print(f"Marks of student {i} in subject {j} is {m2}")
    j += 1
    print(f"Marks of student {i} in subject {j } is {m3}")
    i += 1

# Writing multiple lines in a file
f = open("lines.txt", "w")
my_list = ["line1\n", "line2\n", "line3"]
f.writelines(my_list)
f.close()


# Seek
f = open("temp.txt", "r")
f.seek(9)  # counting starts from 1, moves the pointer to 9th postition
print("Postion of file pointer: ", f.tell())
print(f.read(6))  # will read next 6 characters

# with open("temp.txt", "w") as f:
#     f.write("Helloooo")
#     f.truncate(4) # Will print Hell
