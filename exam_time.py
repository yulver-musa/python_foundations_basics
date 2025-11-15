exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

status = ""

exam_hour_minutes = (60 * exam_hour)
exam_total_minutes = exam_hour_minutes + exam_minutes
arrival_hour_minutes = (60 * arrival_hour)
arrival_total_minutes = arrival_hour_minutes + arrival_minutes

exam_limit = exam_total_minutes - 30

diff_total_minutes = abs(arrival_total_minutes - exam_total_minutes)
diff_total_hours = 0
diff_left_minutes = 0

if arrival_total_minutes > exam_total_minutes:
    status = "Late"
elif exam_limit <= arrival_total_minutes <= exam_total_minutes:
    status = "On time"
elif arrival_total_minutes < exam_total_minutes:
    status = "Early"

if diff_total_minutes >= 60:
    diff_total_hours = diff_total_minutes // 60
    diff_left_minutes = diff_total_minutes % 60

if status == "Late":
    if diff_total_minutes < 60:
        print(status)
        print(f"{diff_total_minutes} minutes after the start")
    else:
        if 0 <= diff_left_minutes < 10:
            print(status)
            print(f"{diff_total_hours}:0{diff_left_minutes} hours after the start")
        else:
            print(status)
            print(f"{diff_total_hours}:{diff_left_minutes} hours after the start")
elif status == "On time":
    print(status)
    print(f"{diff_total_minutes} minutes before the start")
elif status == "Early":
    if diff_total_minutes < 60:
        print(status)
        print(f"{diff_total_minutes} minutes before the start")
    else:
        if 0 <= diff_left_minutes < 10:
            print(status)
            print(f"{diff_total_hours}:0{diff_left_minutes} hours before the start")
        else:
            print(status)
            print(f"{diff_total_hours}:{diff_left_minutes} hours before the start")
