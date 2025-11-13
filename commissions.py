city = input()
sales = float(input())

commissions = 0
valid = True

if city == "Sofia":
    if 0 <= sales <= 500:
        commissions = 0.05
    elif 500 < sales <= 1000:
        commissions = 0.07
    elif 1000 < sales <= 10000:
        commissions = 0.08
    elif 10000 < sales:
        commissions = 0.12
    elif sales < 0:
        print("error")
        valid = False
elif city == "Varna":
    if 0 <= sales <= 500:
        commissions = 0.045
    elif 500 < sales <= 1000:
        commissions = 0.075
    elif 1000 < sales <= 10000:
        commissions = 0.10
    elif 10000 < sales:
        commissions = 0.13
    elif sales < 0:
        print("error")
        valid = False
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commissions = 0.055
    elif 500 < sales <= 1000:
        commissions = 0.08
    elif 1000 < sales <= 10000:
        commissions = 0.12
    elif 10000 < sales:
        commissions = 0.145
    elif sales < 0:
        print("error")
        valid = False
else:
    print("error")
    valid = False

if valid:
    salary = sales * commissions
    print(f"{salary:.2f}")
