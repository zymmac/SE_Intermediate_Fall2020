#Addition

first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
try:
    addition = int(first_num) + int(second_num)
except ValueError:
    print("You have to enter two numbers! Start over.")
else:
    print(f'{first_num} + {int(second_num)} = {addition}')
    print('End of program. Thanks!')

