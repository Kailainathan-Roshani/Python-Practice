# Hotel Billing System

menu = {
    1: {"item": "Burger", "price": 800},
    2: {"item": "Pizza", "price": 1500},
    3: {"item": "Fried Rice", "price": 1200},
    4: {"item": "Chicken Kottu", "price": 1000},
    5: {"item": "Soft Drink", "price": 300}
}

total = 0
bill = []

print("=" * 45)
print("        WELCOME TO ABC HOTEL")
print("=" * 45)

while True:

    print("\n--------- MENU CARD ---------")
    for key, value in menu.items():
        print(f"{key}. {value['item']} - Rs.{value['price']}")

    choice = int(input("\nEnter Item Number: "))

    if choice not in menu:
        print("Invalid Item!")
        continue

    qty = int(input("Enter Quantity: "))

    item = menu[choice]["item"]
    price = menu[choice]["price"]

    amount = qty * price
    total += amount

    bill.append([item, qty, price, amount])

    again = input("\nDo you want to order more? (yes/no): ").lower()

    if again != "yes":
        break

gst = total * 0.10
grand_total = total + gst

print("\n")
print("=" * 50)
print("              FINAL RECEIPT")
print("=" * 50)

print("{:<20}{:<10}{:<10}{:<10}".format("Item", "Qty", "Price", "Amount"))

for row in bill:
    print("{:<20}{:<10}{:<10}{:<10}".format(row[0], row[1], row[2], row[3]))

print("-" * 50)
print(f"Subtotal       : Rs.{total:.2f}")
print(f"GST (10%)      : Rs.{gst:.2f}")
print(f"Grand Total    : Rs.{grand_total:.2f}")
print("=" * 50)

print("\nThank You! Visit Again 😊")