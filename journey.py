budget = float(input())
season = input()

expenditures = 0
destination = ""
accommodation = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        expenditures = budget * 0.3
    elif season == "winter":
        accommodation = "Hotel"
        expenditures = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        expenditures = budget * 0.4
    elif season == "winter":
        accommodation = "Hotel"
        expenditures = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    accommodation = "Hotel"
    expenditures = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{accommodation} - {expenditures:.2f}")
