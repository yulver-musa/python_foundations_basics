movie_type = input()
rows = int(input())
columns = int(input())

ticket = 0

capacity = rows * columns

income = 0
if movie_type == "Premiere":
    ticket = 12
    income = capacity * ticket
elif movie_type == "Normal":
    ticket = 7.5
    income = capacity * ticket
elif movie_type == "Discount":
    ticket = 5
    income = capacity * ticket

print(f"{income:.2f} leva")
