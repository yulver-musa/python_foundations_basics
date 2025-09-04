vacation_cost = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.6
doll_price = 3
bear_prize = 4.1
minion_prize = 8.2
truck_prize = 2

total_puzzle = puzzles_count * puzzle_price
total_doll = dolls_count * doll_price
total_bear = bears_count * bear_prize
total_minion = minions_count * minion_prize
total_truck = trucks_count * truck_prize

sub_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count

sub_total = total_puzzle + total_doll + total_bear + total_minion + total_truck

if sub_count >= 50:
    sub_total = sub_total * 0.75

sub_total = sub_total * 0.9

difference = abs(vacation_cost - sub_total)

if sub_total >= vacation_cost:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
