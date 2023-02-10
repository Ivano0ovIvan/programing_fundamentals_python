quantity_food_gr = float(input()) * 1000
quantity_hay_gr = float(input()) * 1000
quantity_cover_gr = float(input()) * 1000
guineas_weight_gr = float(input()) * 1000

flag = False
for day in range(1, 31):
    quantity_food_gr -= 300

    if day % 2 == 0:
        quantity_hay_gr -= quantity_food_gr * 0.05
    if day % 3 == 0:
        quantity_cover_gr -= guineas_weight_gr / 3
    if quantity_food_gr <= 0 or quantity_hay_gr <= 0 or quantity_cover_gr <= 0:
        flag = True
        break
if not flag:
    food, hay, cover = quantity_food_gr / 1000, quantity_hay_gr / 1000, quantity_cover_gr / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")