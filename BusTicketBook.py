import random
from datetime import datetime

# -----------------------------
# Bus Details
# -----------------------------
buses = {
    1: {"route": "Colombo -> Jaffna", "price": 2500},
    2: {"route": "Colombo -> Kandy", "price": 1200},
    3: {"route": "Colombo -> Galle", "price": 1000},
    4: {"route": "Jaffna -> Trincomalee", "price": 1800},
    5: {"route": "Kandy -> Batticaloa", "price": 2000}
}

print("=" * 50)
print("        BUS TICKET BOOKING SYSTEM")
print("=" * 50)

# -----------------------------
# Customer Details
# -----------------------------
name = input("Enter Passenger Name : ")
phone = input("Enter Phone Number   : ")

print("\nAvailable Buses")
print("-" * 50)

for key, value in buses.items():
    print(f"{key}. {value['route']}  -  Rs.{value['price']}")

choice = int(input("\nSelect Bus (1-5): "))

if choice not in buses:
    print("Invalid Bus Selection!")
    exit()

selected_route = buses[choice]["route"]
ticket_price = buses[choice]["price"]

print("\nSelected Route :", selected_route)
print("Ticket Price   : Rs.", ticket_price)

seat = input("\nEnter Seat Number : ").upper()

tickets = int(input("Number of Tickets : "))

total = ticket_price * tickets

print("\nTotal Amount : Rs.", total)