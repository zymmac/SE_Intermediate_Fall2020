from os.path import dirname, join
current_dir = dirname(__file__)
filename = 'pi_digits.txt'
file_path = join(current_dir, filename)


with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
