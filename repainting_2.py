# Program Task:
# Write a program that calculates the total cost of renovation, given the following prices:
# • Protective nylon: 1.50 BGN per square meter
# • Paint: 14.50 BGN per liter
# • Paint thinner: 5.00 BGN per liter
#
# Additional rules:
# • Add 10% more paint than needed
# • Add 2 extra square meters of nylon
# • Add 0.40 BGN for bags
# • The labor cost for 1 hour of work is equal to 30% of the total cost of the materials
#
# Input:
# The input comes from the console, with exactly 4 lines:
# 1. Required nylon in square meters (integer, [1…100])
# 2. Required paint in liters (integer, [1…100])
# 3. Required thinner in liters (integer, [1…30])
# 4. Hours needed for the workers to finish the job (integer, [1…9])
#
# Output:
# Print a single line to the console:
# • "{the total cost of the renovation}"

cover = int(input())
paint = int(input())
diluter = int(input())
labour_hours = int(input())

extra_paint = paint * 0.1
extra_cover = 2
bags = 0.4

cover_price = 1.5
paint_price = 14.5
diluter_price = 5

cover_total_price = (cover + extra_cover) * cover_price
paint_total_price = (paint + extra_paint) * paint_price
diluter_total_price = diluter * diluter_price

material_total = cover_total_price + paint_total_price + diluter_total_price + bags

labour_price = material_total * 0.3

labour_total_price = labour_price * labour_hours

total_cost = material_total + labour_total_price

print(f'{total_cost:.2f}')
