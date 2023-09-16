print("Calculator cmd v0.1")

def calculate_add():
    value1 = int(input("First value: "))
    value2 = int(input("Second value: "))
    print(value1 + value2)
def calculate_subtract():
    value1 = int(input("First value: "))
    value2 = int(input("Second value: "))
    print(value1 - value2)
def calculate_multiply():
    value1 = int(input("First value: "))
    value2 = int(input("Second value: "))
    print(value1 * value2)
def calculate_divide():
    value1 = int(input("First value: "))
    value2 = int(input("Second value: "))
    print(value1/value2)



while True:

    print(
        '''Select mode: 
        Add = 1
        Subtract = 2
        Multiply = 3
        Divide = 4
        ''')

    v1 = input("Select: ")

    if v1 == '1':
        print("Add Mode")
        calculate_add()
        option = input("Continue?(y/n)")
        if option == 'n':
            break
        elif option == 'y':
            continue

    elif v1 == '2':
        print("Subtract mode")
        calculate_subtract()
        option = input("Continue?(y/n)")
        if option == 'n':
            break
        elif option == 'y':
            continue

    elif v1 == '3':
        print("Multiply Mode")
        calculate_multiply()
        option = input("Continue?(y/n)")
        if option == 'n':
            break
        elif option == 'y':
            continue

    elif v1 == '4':
        print("Divide Mode")
        calculate_divide()
        option = input("Continue?(y/n)")
        if option == 'n':
            break
        elif option == 'y':
            continue


    else:
        print("Please select again")
        continue
