biscuits_per_worker_per_day = int(input())
count_of_workers = int(input())
competing_factory_biscuits = int(input())
produced_biscuits = 0
days_to_produce = 30
for day in range(days_to_produce):
    if day % 3 == 0:
        produced_biscuits += int((count_of_workers * biscuits_per_worker_per_day) * 0.75)
    else:
        produced_biscuits += count_of_workers * biscuits_per_worker_per_day
print(f'You have produced {produced_biscuits} biscuits for the past month.')
difference = produced_biscuits - competing_factory_biscuits
difference_in_percent = (abs(difference) / competing_factory_biscuits) * 100
if difference > 0:
    print(f'You produce {difference_in_percent:.2f} percent more biscuits.')
elif difference < 0:
    print(f'You produce {difference_in_percent:.2f} percent less biscuits.')