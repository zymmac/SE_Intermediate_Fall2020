# GUEST BOOK
filename = 'chapter_10\guest_book.txt'

while True:
    print('Enter your name: ')
    print('Enter "q" to quit')
    name = input()
    if name == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + '\n')
        print(f'Hello, {name}! Welcome!\n')
