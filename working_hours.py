hour = int(input())
day = input()

if 10 <= hour <= 18:
    if day == "Monday" or day == "Tuesday" or day == "Wednesday":
        print("open")
    elif day == "Sunday":
        print("closed")
