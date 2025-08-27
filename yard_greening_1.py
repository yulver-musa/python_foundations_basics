total_area = float(input())

price_per_sq = 7.61

discount = 0.18

subtotal = total_area * price_per_sq

discount_total = subtotal * discount

total = subtotal - discount_total

print(f'The total price is: {total:.2f} lv.')
print(f'The discount is: {discount_total:.2f} lv.')
