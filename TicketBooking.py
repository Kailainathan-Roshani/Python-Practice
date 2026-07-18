# Movie Ticket Booking System

movies = {
    1: {"name": "Leo", "price": 1200},
    2: {"name": "Jailer", "price": 1000},
    3: {"name": "GOAT", "price": 1500},
    4: {"name": "Coolie", "price": 1800}
}

print("=" * 40)
print("      MOVIE TICKET BOOKING")
print("=" * 40)

print("\nAvailable Movies")
for key, value in movies.items():
    print(f"{key}. {value['name']} - Rs.{value['price']}")

choice = int(input("\nSelect Movie (1-4): "))

if choice not in movies:
    print("Invalid Movie Selection!")
    exit()

movie = movies[choice]["name"]
price = movies[choice]["price"]

print("\nAvailable Seats")
print("A1  A2  A3  A4  A5")
print("B1  B2  B3  B4  B5")
print("C1  C2  C3  C4  C5")

seat = input("\nEnter Seat Number: ").upper()

tickets = int(input("Enter Number of Tickets: "))

total = price * tickets

print("\nDo you want Popcorn?")
print("1. Yes (Rs.500)")
print("2. No")

snack = int(input("Choice: "))

snack_price = 0

if snack == 1:
    snack_price = 500

grand_total = total + snack_price

print("\n" + "=" * 40)
print("            BILL")
print("=" * 40)
print("Movie           :", movie)
print("Seat            :", seat)
print("Tickets         :", tickets)
print("Ticket Price    : Rs.", price)
print("Ticket Total    : Rs.", total)
print("Snack           : Rs.", snack_price)
print("-" * 40)
print("Grand Total     : Rs.", grand_total)
print("=" * 40)

print("\nThank You! Enjoy Your Movie 🎬")