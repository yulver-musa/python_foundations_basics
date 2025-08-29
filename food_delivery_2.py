# Restaurant menus: chicken 10.35, fish 12.40, veg 8.15.
# Dessert = 20% of total (before delivery). Delivery = 2.50.
# Input: count chicken, fish, veg.
# Output: final order price.

chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

chicken_price = 10.35
fish_price = 12.4
veggie_price = 8.15
delivery = 2.5

chicken_total = chicken_menu * chicken_price
fish_total = fish_menu * fish_price
veggie_total = veggie_menu * veggie_price

food_subtotal = chicken_total + fish_total + veggie_total

dessert_price = food_subtotal * 0.20
total_food = food_subtotal + dessert_price + delivery

print(f'{total_food:.2f}')