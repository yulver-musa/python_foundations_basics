# George must finish a book in time.
# Input: pages, pages/hour, days.
# Output: hours/day needed for reading.

count_of_pages = int(input())
pages_per_hour = int(input())
count_of_days = int(input())

total_hours = count_of_pages / pages_per_hour
per_day = total_hours / count_of_days

rounded = round(per_day)

print(rounded)