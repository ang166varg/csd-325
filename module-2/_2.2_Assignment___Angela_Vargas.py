def main(): 
    intro() 
    while True:
        try:
            cups_needed = int(input('Enter the number of cups: '))
            if cups_needed <0:#corrected to be only positive numbers
                raise ValueError
            cups_to_ounces(cups_needed)
        except ValueError:
            print("Invalid input. Please enter a numeric value for cups.")

        try:
            gallons_needed = float(input('Enter the number of gallons: '))
            if gallons_needed< 0: #corrected to be only positive numbers
              raise ValueError
            gallons_to_liters(gallons_needed)
        except ValueError:
            print("Invalid input. Please enter a numeric value for gallons.")

def intro():
    print('This program converts measurements')
    print('in cups to fluid ounces and gallons to liters.')
    print('For your reference:')
    print(' 1 cup = 8 fluid ounces')
    print(' 1 gallon = 3.78541 liters')
    print()


def cups_to_ounces(cups):
    ounces = cups * 8
    print('That converts to', ounces, 'ounces.')


def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    print('This converts to', liters , 'liters!')

main()
