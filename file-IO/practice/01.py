#Check word in a file
with open('poem.txt') as f:
    data = f.read()
    if 'Twinkle' in data:
        print("The word 'Twinkle' is present in the file.")
    else:
        print("The word 'Twinkle' is not present in the file.")