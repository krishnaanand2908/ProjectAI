import os
folder = os.listdir("C:\\Users\\consu\\Desktop\\Project AI\\Z-PARTH")
for item in folder:
    if item != "tests.py":
        os.remove(item)