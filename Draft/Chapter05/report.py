# модуль report
from random import choice

possobilities = ["дождь", "снег", "мокрый снег", "туман", "солнце", "кто знает"]


def get_description():
    """Возвращает случайную погоду"""
    return choice(possobilities)
