tv_show = input()
show_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration * 0.125
rest_duration = break_duration * 0.25
free_time = break_duration - lunch_duration - rest_duration

difference = abs(break_duration - free_time)

if break_duration >= free_time:
    print(f"You have enough time to watch {tv_show} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show}, you need {difference} more minutes.")
