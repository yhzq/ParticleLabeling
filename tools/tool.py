import os, glob
path = os.getcwd()
if path.find("\\\\") != -1:
    path += "\\\\"
else:
    path += "/"
print("This tool is designed to conver path in .json files for labeling.")
print("Input Y if you want to change the path to the current path : " + path)
s = input("Input N if you want to change the path to manuel input : ")
if s == "N":
    path = input("The path you want to change to:")
for file in glob.glob("*.json"):
    with open(file, "r") as f:
        line = f.readline()
        newline = line[:line.find(":") + 2] + path + line[line.find(",") - 1 - (len(file) - 1):]
    with open(file, "w") as f:
        f.write(newline)

