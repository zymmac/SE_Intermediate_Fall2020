#Cats and Dogs

filenames = ['chapter_10\cats.txt', 'chapter_10\dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            for line in f:
                print(line.rstrip())
    except FileNotFoundError:
        print(f'{filename} is not found!')