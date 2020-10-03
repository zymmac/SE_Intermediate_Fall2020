#Common Words

filenames = [
                'Charles_Dickens_A_Tale_of_Two_Cities.txt',
                'Mark_Twain_Adventures_of_Huckleberry_Finn.txt',
                'Washington_Irving_The_Legend_of_Sleepy_Hollow.txt'
                ]

for filename in filenames:
    with open(filename,  encoding='utf-8') as f:
        content = f.read()
        case_sensitive = content.count("the")
        case_insensitive = content.lower().count("the")
        specific = content.lower().count(" the ")

        print(f'File read: {filename}')
        print(f'There are {case_sensitive} times the letters "the" appear together (case sensitive).')
        print(f'There are {case_insensitive} times the letters "the" appear together (case insensitive).')
        print(f'There are {specific} times the word "the" appear in the text (case insensitive).\n')