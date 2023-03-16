import logging
logging.basicConfig(level=logging.INFO)

accesories={'saddle pad':[5, 100], 'reins':[6, 230], 'saddle':[10, 543], 'bellyband':[11, 150]}


def accesories_magazine(option):
    if option==1:
        print("List of products:")
        for keys, values in accesories.items():
           list=print(f"name: {keys}, quantity available {values[0]}, price in PLN per piece: {values[1]}")
        return f'Done!'
    elif option==2:
        name=input('Enter the product name:')
        if name in accesories.keys():
            values=accesories[name]
            return f"Product name {name}, quantity available {values[0]} price in PLN per piece: {values[1]}"


def accesories_magazine_quantity(option_2, name, quantity):
    if option_2==1:
        new_quantity = accesories[name][0]-quantity
        if name in accesories.keys():
            accesories[name][0]=[new_quantity]
        return f'The current quantity for the product {name} is {accesories[name][0]}'
    elif option_2 == 2:
        new_quantity = quantity + accesories[name][0]
        if name in accesories.keys():
            accesories[name][0]=[new_quantity]
        return f'The current quantity for the product {name} is {accesories[name][0]}'


def accesories_magazine_update(option_2):
    if option_2 == 3:
        accesories[name][1]=[new_price]
        return f'Product {name} new price in PLN pre piece is {new_price}'
    else:
        print('No product in system')
        exit()


if __name__=='__main__':
    option=int(input('Helo! \n 1. List of product\n 2. Search for a product\nEnter number:'))
    accesories_menu=accesories_magazine(option)
    print(accesories_menu)
    option_2=int(input('What do you wana to do next?\n1. Remove from magazine\n2. Add to the magazine\n3. Update price \nEnter number:  '))
    name=input('Enter the product name:')
    if option_2==1 or 2:
        quantity=int(input('Enter quantity:'))
        print(accesories_magazine_quantity(option_2, name, quantity))
    if option_2==2:
        quantity=int(input('Enter quantity:'))
        accesories_magazine_quantity(option_2, name, quantity)
    elif option_2==3:
        new_price=input('Enter new price:')
        print(accesories_magazine_update(option_2))

