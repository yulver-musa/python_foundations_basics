budget = int(input())
season = input()
count = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
    if count <= 6:
        boat_rent *= 0.90
    elif 6 < count <= 11:
        boat_rent *= 0.85
    elif count >= 12:
        boat_rent *= 0.75

elif season == "Summer":
    boat_rent = 4200
    if count <= 6:
        boat_rent *= 0.90
    elif 6 < count <= 11:
        boat_rent *= 0.85
    elif count >= 12:
        boat_rent *= 0.75

elif season == "Autumn":
    boat_rent = 4200
    if count <= 6:
        boat_rent *= 0.90
    elif 6 < count <= 11:
        boat_rent *= 0.85
    elif count >= 12:
        boat_rent *= 0.75
elif season == "Winter":
    boat_rent = 2600
    if count <= 6:
        boat_rent *= 0.90
    elif 6 < count <= 11:
        boat_rent *= 0.85
    elif count >= 12:
        boat_rent *= 0.75

if count % 2 == 0 and season != "Autumn":
    boat_rent *= 0.95

difference = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
