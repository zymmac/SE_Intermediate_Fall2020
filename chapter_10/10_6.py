#Addition Calculator

while True:
    print("Enter 'q' to exit the program")
    first_num = input("Enter the first number: ")
    if first_num.lower() == 'q':
        print("End of program. Thanks!")
        break

    second_num = input("Enter the second number: ")
    if second_num.lower() == 'q':
        print("End of program. Thanks!")
        break

    try:
        addition = int(first_num) + int(second_num)
    except ValueError:
        print("You have to enter two numbers! Start over.\n")
    else:
        print(f'{first_num} + {int(second_num)} = {addition}')
        print('')
