filename = 'chapter_10\why_like.txt'

while True:
    print('Enter "q" to quit the program.')
    reason = input("Why do you like programming? ")
    if reason.lower() == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(reason)
            f.write('\n')
