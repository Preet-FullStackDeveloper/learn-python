# This code demonstrates how to use the `with` statement for file I/O in Python.
# Using 'with' statement for file I/O
with open('file.txt', 'r') as f:
    data = f.read()
    print(data)