week_day = input()

if week_day == "Monday" or week_day == "Tuesday" or week_day == "Wednesday"\
        or week_day == "Thursday" or week_day == "Friday":
    print("Working day")
elif week_day == "Saturday" or week_day == "Sunday":
    print("Weekend")
else:
    print("Error")
