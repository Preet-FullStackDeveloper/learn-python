f = open('myFile.txt')
data  = f.readlines()
print(type(data))  # This will show that data is a list of lines
print(data)
# Print each line from the list
for line in data:
    print(line.strip())
f.close()