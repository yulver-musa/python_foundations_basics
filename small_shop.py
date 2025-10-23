item = input()
city = input()
qty = float(input())


if city == "Sofia":
    if item == "coffee":
        price = 0.5
    elif item == "water":
        price = 0.8
    elif item == "beer":
        price = 1.2
    elif item == "sweets":
        price = 1.45
    elif item == "peanuts":
        price = 1.6
elif city == "Plovdiv":
    if item == "coffee":
        price = 0.4
    elif item == "water":
        price = 0.7
    elif item == "beer":
        price = 1.15
    print("null")
elif city == "Varna":
    print("null")
