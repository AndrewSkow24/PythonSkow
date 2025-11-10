# 1. Сколько секунд в часе? Используйте интерактивный интерпретатор как калькулятор и умножьте количество
# секунд в минуте (60) на количество минут в часе (тоже 60).
print("Task 1")
print("Секунд в часе:", 60 * 60)

# 2. Присвойте результат вычисления предыдущего задания (секунды в часе) переменной,
# которая называется seconds_per_hour.
print("Task 2")
seconds_per_hour = 60 * 60
print("Значение переменной seconds_per_hour:", seconds_per_hour)

# 3. Сколько секунд в сутках? Используйте переменную seconds_per_hour.
print("Task 3")
print("Секунд в сутках:", seconds_per_hour * 24)

# 4. Снова посчитайте количество секунд в сутках, но на этот раз сохраните результат в переменной seconds_per_day.
print("Task 4")
seconds_per_day = seconds_per_hour * 24
print("Значение переменной seconds_per_day:", seconds_per_day)

# 5. Разделите значение переменной seconds_per_day на значение переменной seconds_per_hour.
# Используйте деление с плавающей точкой (/).
print("Task 5")
print(
    f"Деление с плавающей точкой (/) seconds_per_day на seconds_per_hour: {seconds_per_day/seconds_per_hour}"
)

# 6. Разделите значение переменной seconds_per_day на значение переменной seconds_per_hour.
# Используйте целочисленное деление (//). Совпадает ли полученный результат с ответом на предыдущее упражнение,
# если не учитывать символы .0 в конце?
print("Task 6")
print(
    f"Целочисленное деление (//) seconds_per_day на seconds_per_hour: {seconds_per_day//seconds_per_hour}"
)
print(
    "Равны ли результаты: ",
    seconds_per_day / seconds_per_hour == seconds_per_day // seconds_per_hour,
)
