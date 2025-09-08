# Swimming record: given record time, distance, and time per meter.
# Every 15m Ivan slows by 12.5s.
# Calculate total time and check if he beats the record.

import math
record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

sub_seconds = distance_meters * seconds_per_meter
part = math.floor(distance_meters / 15)
extra = part * 12.5
total_time = sub_seconds + extra

diff = total_time - record_seconds

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
