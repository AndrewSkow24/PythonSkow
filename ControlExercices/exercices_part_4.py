# 1. Присвойте значение 7 переменной guess_me. Далее напишите условные проверки (if, else и elif),
# чтобы вывести строку 'too low', если значение переменной guess_me меньше 7, 'too high',
# если оно больше 7, и 'just right', если равно 7.
from itertools import count

print("Task 1")
guess_me = 7
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else:
    print("just right")

# 2. Присвойте значение 7 переменной guess_me и значение 1 переменной start.
# Напишите цикл while, который сравнивает переменные start и guess_me. Выведите строку 'too low',
# если значение переменной start меньше значения переменной guess_me.
# Если значение переменной start равно значению переменной guess_me, выведите строку 'found it!' и выйдите из цикла.
# Если значение переменной start больше значения переменной guess_me, выведите строку 'oops' и выйдите из цикла.
# Увеличьте значение переменной start на выходе из цикла.
print("Task 2")
guess_me = 7
start = 1

while start <= guess_me:
    if start < guess_me:
        print("too low")
    elif start == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    start += 1

# 3. Используйте цикл for, чтобы вывести на экран значения списка [3, 2, 1, 0].
print("Task 3")
list_numbers = [3, 2, 1, 0]
for num in list_numbers:
    print(num)

# 4. Используйте включение списка, чтобы создать список, который содержит нечетные числа в диапазоне range(10).
print("Task 4")
comprehension_list = [num for num in range(10) if num % 2 != 0]
print(comprehension_list)

# 5. Используйте включение словаря, чтобы создать словарь squares. Используйте
# вызов range(10), чтобы получить ключи, и возведите их в квадрат, чтобы получить их значения.
print("Task 5")
comprehension_dictionary = {num: num**2 for num in range(10)}
print(comprehension_dictionary)

# 6. Используйте включение множества, чтобы создать множество odd, которое содержит четные числа в диапазоне range(10).
print("Task 6")
# создание множества чётных чисел
odd = {num for num in range(10) if num % 2 == 0}
print(odd)

# 7. Используйте включение генератора, чтобы вернуть строку 'Got' и количество
# чисел в диапазоне range(10). Итерируйте по нему с помощью цикла for.
# создание включение генератора
print("Task 7")
count_numbers = 0
comprehension_generator = (number for number in range(10))
for i in comprehension_generator:
    count_numbers += 1
print(f"got: {count_numbers}")


# 8. Определите функцию good, которая возвращает список ['Harry', 'Ron', 'Hermione'].
def good():
    return ["Harry", "Ron", "Hermione"]


print(good())


# 9. Определите функцию генератора get_odds, которая возвращает четные числа из
# диапазона range(10). Используйте цикл for, чтобы найти и вывести третье возвращенное значение.
print("Tak 9")


def get_odds(start=0, stop=10, step=2):
    num = start
    while num < stop:
        yield num
        num += step


my_genetator = get_odds()
print("Третье значение из генератора:", [num for num in my_genetator][2])


# 10. Определите декоратор test, который выводит строку 'start', когда вызывается
# функция, и строку 'end', когда функция завершает свою работу.
def test(func):
    def new_function(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("stop")
        return func(*args, **kwargs)

    return new_function


@test
def primitve_func(str):
    print(str)
    return str


primitve_func("Текст декоратора")
returned_of_primitive_func = primitve_func("Returned value")
print("Возвращаемое значение:", returned_of_primitive_func)

# 11. Определите исключение, которое называется OopsException. Сгенерируйте его,
# чтобы увидеть, что произойдет. Затем напишите код, позволяющий поймать это
# исключение и вывести строку 'Caught an oops'.

print("Task 11")


class OopsException(Exception):
    pass


try:
    raise OopsException("Caught an oops")
except OopsException as e:
    print(e)


# 12. Используйте функцию zip(), чтобы создать словарь movies, который объединя-
# ет в пары эти списки: titles = ['Creature of Habit', 'Crewel Fate'] и plots = ['A nun
# turns into a monster', 'A haunted yarn shop'].
print("Task 12")
titles = ["Creature of Habit", "Crewel Fate"]
plots = ["A nunturns into a monster", "A haunted yarn shop"]
movies = {}
for value, key in zip(titles, plots):
    movies[value] = key
print(movies)
