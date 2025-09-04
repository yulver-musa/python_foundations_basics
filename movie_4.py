# Calculates movie expenses (decor + costumes with discount)
# and checks if the budget is enough.

movie_budget = float(input())
crew_member = int(input())
costume_price = float(input())

decor = movie_budget * 0.1
if crew_member > 150:
    costume_price = costume_price * 0.9

total_costumes = crew_member * costume_price

total_expenditures = total_costumes + decor

difference = abs(movie_budget - total_expenditures)

if movie_budget >= total_expenditures:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
