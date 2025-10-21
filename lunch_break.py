import math

tv_show = input()
show_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration * 0.125
rest_duration = break_duration * 0.25
free_time = break_duration - lunch_duration - rest_duration

difference = abs(show_duration - free_time)

if free_time >= show_duration:
    print(f"You have enough time to watch {tv_show} and left with {math.ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show}, you need {math.ceil(difference)} more minutes.")
