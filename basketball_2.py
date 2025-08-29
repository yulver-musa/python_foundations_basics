# Jesse trains basketball. Input: yearly fee.
# Shoes = 60% fee, outfit = 80% shoes, ball = 1/4 outfit, accessories = 1/5 ball.
# Output: total cost.

yearly_cost = int(input())

shoes_cost = yearly_cost - (yearly_cost * 0.4)
suit_cost = shoes_cost - (shoes_cost * 0.2)
ball_cost = suit_cost * 0.25
accessories_cost = ball_cost * 0.2

total_cost = yearly_cost + shoes_cost + suit_cost + ball_cost + accessories_cost

print(f'{total_cost:.2f}')
