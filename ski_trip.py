days = int(input())
accommodation = input()
evaluation = input()

price = 0
nights = days - 1
total = 0

if accommodation == "room for one person":
    price = 18
    total = nights * price
    if evaluation == "positive":
        total *= 1.25
    elif evaluation == "negative":
        total *= 0.9
elif accommodation == "apartment":
    price = 25
    total = nights * price
    if nights < 10:
        total *= 0.7
    elif 10 <= nights <= 15:
        total *= 0.65
    elif nights > 15:
        total *= 0.5

    if evaluation == "positive":
        total *= 1.25
    elif evaluation == "negative":
        total *= 0.9
elif accommodation == "president apartment":
    price = 35
    total = nights * price
    if nights < 10:
        total *= 0.9
    elif 10 <= nights <= 15:
        total *= 0.85
    elif nights > 15:
        total *= 0.8

    if evaluation == "positive":
        total *= 1.25
    elif evaluation == "negative":
        total *= 0.9

print(f"{total:.2f}")
