#Deine the menu of the hotel
menu = {
    'Pizza':40,
    'Burger':50,
    'Pasta':60,
    'Salad':80,
    'Coffee':30
}
#Greet
print('welcome to Python Resturant')
print('Pizza: Rs.40\nBurger: Rs.50\nPasta: Rs.60\nSalad: Rs.80\nCoffee: Rs.30')

order_total = 0

item_1 = input('Enter the Name of item you want to order ==')
if item_1 in menu:
    order_total +=  menu[item_1]
    print('Your item  has been added to your order',item_1)

else:
    print('Odered item is not available yet !!!',item_1)

another_order = input('Do you want to add another item? (Yes/No)')
if another_order == 'Yes':
    item_2 = input('Enter the name of second item = ')
    if item_2 in menu:
        order_total += menu[item_2]
        print('Item  has been added to order',item_2)
    else:
        print('Ordered item  is not available!!',item_2)

print('The total amount of items to pay is ',order_total)
