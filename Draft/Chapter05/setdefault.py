periodic_table = {"Водород": 1, "Гелий": 2}
print(periodic_table)
carbon = periodic_table.setdefault("Углерод", 14)
print(carbon)
print(periodic_table)
helium = periodic_table.setdefault("Гелий", 947)
print(helium)  # 2 - так как такой ключ уже существует и новое значение не приписывается

"""
Функция defaultdict() похожа на предыдущую, но она опредлеляет значение 
по умолчанию для новых ключей заранее, при создании словаря. В этом примере 
мы предлагаем функцию int() и возвращаем значение
"""

from collections import defaultdict

periodic_table = defaultdict(int)

periodic_table["Водород"] = 1
periodic_table["Свинец"]
periodic_table["Медь"]
print(periodic_table)


def no_idea():
    return "Нет значения"


bestiary = defaultdict(no_idea)

bestiary["a"] = "снежный челоек"
bestiary["b"] = "базилик"
bestiary["c"]

print(bestiary)
