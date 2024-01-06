import os
folders = os.listdir("D:\MOVIES")


# print(folders)

for folder in folders:
    print(os.listdir(f"D:\MOVIES{folder}"))