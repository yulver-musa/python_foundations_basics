sum_for_deposit = float(input())
deposit_period = int(input())
yearly_rate = float(input())

percentage_yearly_late = yearly_rate / 100

rate = sum_for_deposit * percentage_yearly_late

rate_per_month = rate / 12

total = sum_for_deposit + deposit_period * rate_per_month

print(f'{total:.2f}')
