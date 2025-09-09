budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = 250
gpu_cost = gpu_count * gpu_price

cpu_price = gpu_cost * 0.35
cpu_cost = cpu_count * cpu_price

ram_price = gpu_cost * 0.1
ram_cost = ram_count * ram_price

sub_cost = gpu_cost + cpu_cost + ram_cost

if gpu_count > cpu_count:
    sub_cost *= 0.85

diff = abs(budget - sub_cost)

