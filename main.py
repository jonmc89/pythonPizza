print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L:\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
extra_cheese = input("D0 you want extra cheese? Y or N:\n")
bill = 0

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    print(f"Your total bill is ${bill}")

elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your total bill is ${bill}")
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your total bill is ${bill}")
else:
    print("You need to choose S, M or L!")
