import os

if not os.path.exists("data"):
    os.mkdir("data")

# for i in range(5):
#     os.mkdir(f"data/day{i+1}")

# for i in range(5):
#     os.rename(f"data/day{i+1}", f"data/Tutorial{i+1}")

folders = os.listdir("data")
print(len(folders)) #Number of folders in data folder

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}")) #Displays the content inside each folder

# os.remove() #Removes a file
# os.rmdir() #Removes an empty directory
# shutil.rmtree() #Deletes directory and its content
