#from os.path import dirname,join
#current_dir = dirname(__file__)
filename = 'chapter_10\learning_python.txt'
#file_path = join(current_dir,filename)

with open(filename) as f:
    for line in f:
        print(line.replace("Python", "C").rstrip())
