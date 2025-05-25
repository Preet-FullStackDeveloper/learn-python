# Read mode is default, so you can also use `open("file.txt")`
# Read files in Python
f = open("file.txt")
data = f.read()
print(data)
f.close();

# Write files in Python
f = open("myFile.txt", "w")
f.write("Hello, World!\n")
f.write("This is a new line.\n")
f.close()