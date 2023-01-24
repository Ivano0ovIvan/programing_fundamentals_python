count_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = count_of_lost_fights // 2
total_sword_broken = count_of_lost_fights // 3
total_shield_broken = count_of_lost_fights // 6
total_armor_broken = total_shield_broken // 2
expenses = (helmet_price * total_helmet_broken) + (sword_price * total_sword_broken) + (shield_price * total_shield_broken) + (armor_price * total_armor_broken)
print(f"Gladiator expenses: {expenses:.2f} aureus")