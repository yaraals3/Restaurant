MENU = {
    'SIDES': ['french fries', 'rocca salad', 'burrata salad'],
    'MAIN': ['pink pasta', 'ravioli', 'truffle pizza'],
    'DESSERT': ['brownies', 'gelato', 'cheesecake'],
    'DRINKS': ['mojito', 'water', 'sparkling drinks'],
}

PRICES = {
    'french fries': 19.55,
    'rocca salad': 28.99,
    'burrata salad': 34.55,
    'pink pasta': 55.55,
    'ravioli': 60.55,
    'truffle pizza': 70.99,
    'brownies': 27.50,
    'gelato': 15.50,
    'cheesecake': 25.50,
    'mojito': 18.30,
    'water': 5.50,
    'sparkling drinks': 9.50,
}

def show_menu():
    print('Hello to Little Pizza Restaurant!')
    print('Check the menu down below!')
    for category, items in MENU.items():
        print(f'\n**{category.upper()}**')
        for item in items:
            print(f'{item} - ${PRICES[item]:.2f}')

def take_order():
    order = []
    while True:
        item = input('\nWhat would you like to order? (enter "nothing" to quit):').lower().strip()
        if item == 'nothing':
            break
        # Check if the entered item is in the menu items
        if item not in [menu_item for items in MENU.values() for menu_item in items]:
            print('Unfortunately, we don\'t offer that dish/drink. Please see our menu again!')
            continue
        try:
            quantity = int(input(f'How many {item}s would you like to order?'))
        except ValueError:
            print('Please enter a valid quantity (whole number).')
            continue
        order.append((item, quantity))
    return order

def print_order(order):
    if not order:
        print('No items ordered.')
        return
    print('\n**Your order:**')
    total = 0
    for item, quantity in order:
        price = PRICES[item]
        total += price * quantity
        print(f'{quantity}x {item} - ${price * quantity:.2f}')
    print(f'\nTotal: ${total:.2f}')

show_menu()
order = take_order()
print_order(order)
