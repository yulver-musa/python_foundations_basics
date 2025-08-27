# Write a program that calculates the total amount you will receive at the end of a deposit period
# given a certain interest rate. Use the following formula:
# amount = deposited_amount + deposit_period * ((deposited_amount * annual_interest_rate) / 12)
#
# Input
# The program reads 3 lines from the console:
# 1. Deposited amount – a real number in the range [100.00 … 10000.00]
# 2. Deposit period (in months) – an integer in the range [1 … 12]
# 3. Annual interest rate – a real number in the range [0.00 … 100.00]

sum_for_deposit = float(input())
deposit_period = int(input())
yearly_rate = float(input())

percentage_yearly_late = yearly_rate / 100

rate = sum_for_deposit * percentage_yearly_late

rate_per_month = rate / 12

total = sum_for_deposit + deposit_period * rate_per_month

print(f'{total:.2f}')
