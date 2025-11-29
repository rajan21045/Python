menu = {
    "Coffee": 70,
    "Pizza": 50,
    "Sandwich": 150,
    "Pasta": 120,
    "Burger": 100,
    "Salad": 80
}
print("Welcome To The Py Hotel")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: ${price}")

order_total = 0

item_1 = input("Enter the first item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Current total: ${order_total}")
else:
    print(f"Sorry, {item_1} is not on the menu.")
