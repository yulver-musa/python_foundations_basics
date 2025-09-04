# Reads hours and minutes, adds 15 minutes,
# and prints the new time in HH:MM format.

hours = int(input())
minutes = int(input())

extra_minutes = 15

hours_in_minutes = hours * 60

total_minutes = hours_in_minutes + minutes + extra_minutes

final_hours = total_minutes // 60
if final_hours >= 24:
    final_hours = final_hours - 24
final_minutes = total_minutes % 60

if final_minutes < 10:
    print(f'{final_hours}:0{final_minutes}')
else:
    print(f'{final_hours}:{final_minutes}')

