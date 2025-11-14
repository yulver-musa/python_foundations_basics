flowers = input()
count = int(input())
budget = int(input())

price = 0
total = 0

if flowers == "Roses":
    price = 5
    total = count * price
    if count > 80:
        total = (count * price) * 0.9
elif flowers == "Dahlias":
    price = 3.80
    total = count * price
    if count > 90:
        total = (count * price) * 0.85
elif flowers == "Tulips":
    price = 2.80
    total = count * price
    if count > 80:
        total = (count * price) * 0.85
elif flowers == "Narcissus":
    price = 3
    total = count * price
    if count < 120:
        total = (count * price) * 1.15
elif flowers == "Gladiolus":
    price = 2.50
    total = count * price
    if count < 80:
        total = (count * price) * 1.2

difference = abs(budget - total)

if budget >= total:
    print(f"Hey, you have a great garden with {count} {flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
