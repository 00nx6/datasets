def menu():
    print("\n[Menu]")
    print(" 1. Calculate stats")
    print(" 2. Filter the data")
    print(" 3. Clear filter")
    
    while True:
        try:
            usr_nav = int(input('Please select an option'))
            if usr_nav < 1 or usr_nav > 3:
                raise ValueError()
        except ValueError:
            print("ERROR: Not given option")
        else:
            break

    return usr_nav

def get_filter():
    print('How do you wish to filter the data?')
    print(' 1. By pet kind')
    print(' 2. By pet name')
    
    while True:
        try:
            usr_nav = int(input('Please select an option'))
        except ValueError:
            print('ERROR: Enter a number')
        else:
            match usr_nav:
                case 1:
                    filters = filter_by_kind()
                case 2:
                    filters = filter_by_name()
                case _:
                    print("ERROR: Invalid input")
                    continue
            break
    return filters

def filter_by_kind():
    print('Select one of the following kind: ')
    print(' 1. Dog')
    print(' 2. Cat')
    print(' 3. Parrot')
    
    while True:
        try:
            usr_nav = int(input('Please select an option: '))
        except ValueError:
            print('ERROR: Enter a number: ')
        else:
            match usr_nav:
                case 1:
                    filters = ['Dog', '']
                case 2:
                    filters = ['Cat', '']
                case 3:
                    filters = ['Parrot', '']
                case _:
                    print("ERROR: Invalid input")
                    continue
            break
    return filters

def filter_by_name():
    while True:
        try:
            usr_input = input('Please enter a name: ')
            if not usr_input:
                raise ValueError
        except ValueError:
            print('ERROR: Do not leave the field empty.')
        else:
            return ['All', usr_input]
