#from os.path import dirname, join
from os import getcwd
print(getcwd())
#current_dir = dirname(__file__)
filename = 'chapter_10\learning_python.txt'
#file_path = join(current_dir, filename)

with open(filename) as f:
    content = f.read()

print(content)

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

with open(filename) as f:
    for line in f:
        print(line.rstrip())