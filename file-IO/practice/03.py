'''
Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.
'''

def table(i):
    print(f"Generating table for {i}...")
    with open(f"tables/table_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
    print(f"Table of {i} written to table_{i}.txt")

for i in range(2, 4):
    table(i)