filename = 'chapter_10\guest.txt'

name = input('Please, enter your name: ')
with open(filename, 'w') as f:
    f.write(name)
