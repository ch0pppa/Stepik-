current_day = int(input())
current_weight = float(input())
initial_weight = 100
target_weight = 88
total_days = 60
daily_losses = (initial_weight-target_weight)/total_days
target_weight_for_day = initial_weight - (daily_losses * current_day) 
if current_weight <= target_weight_for_day:
    status = "Все идет по плану"
else:
    status = "Что-то пошло не так"
print(status)
print(f"#{current_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {target_weight_for_day:.1f} кг")