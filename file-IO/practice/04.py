'''
A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. 
'''
with open('donkey.txt') as f:
    data = f.read()
    data = data.replace('Donkey', '#####')
with open('donkey.txt', 'w') as f:
    f.write(data)
print("The word 'Donkey' has been replaced with '#####' in the file.")