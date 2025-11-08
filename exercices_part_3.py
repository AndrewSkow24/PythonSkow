# 1. Создайте список years_list, содержащий год, в который вы родились, и каждый
# последующий год вплоть до вашего пятого дня рождения. Например, если вы
# родились в 1980 году, список будет выглядеть так:
# years_list = [1980, 1981, 1982, 1983, 1984, 1985].
# Если вам меньше пяти лет и вы уже читаете эту книгу, то я даже не знаю, что
# сказать.
print("Task 1")
years_list = [1993, 1994, 1995, 1996, 1997, 1998]
print("Список годов:", years_list)

# 2. В какой из годов, содержащихся в списке years_list, был ваш третий день рождения?
# Помните, в первый год вам было 0 лет.
print("Task 2")
print(f"Третий день рождения был в {years_list[3]} году")

# 3. В какой из годов, перечисленных в списке years_list, вам было больше всего лет?
print("Task 3")
print("Наибольший год:", max(years_list))

# 4. Создайте список things, содержащий три элемента: "mozzarella", "cinderella",
# "salmonella".
print("Task 4")
things = ["mozzarella", "cinderella", "salmonella"]
print("Новый список things:", things)

# 5. Напишите с большой буквы тот элемент списка things, который относится
# к человеку, а затем выведите список. Изменился ли элемент списка?
print("Task 5")
things[1] = things[1].capitalize()
print("Обновлённый список:", things)

# 6. Переведите сырный элемент списка things в верхний регистр целиком и выведите список.
print("Task 6")
things[0] = things[0].upper()
print("Обновлённый список:", things)

# 7. Удалите болезнь из списка things, получите Нобелевскую премию и затем выведите список на экран.
print("Task 7")
del things[2]
print("Обновлённый список:", things)

# 8. Создайте список, который называется surprise и содержит элементы 'Groucho','Chico' и 'Harpo'.
print("Task 8")
surprise = ["Groucho", "Chico", "Harpo"]
print("Список surprise:", surprise)

# 9. Напишите последний элемент списка surprise со строчной буквы, затем обратите его и напишите с прописной буквы.
print("Task 9")
element = surprise[-1].lower()  # cделали первую букву строчной
element = list(element)  # преобразовали к списку для применения реверса
element.reverse()  # применили реверс
element = "".join(element).capitalize()
surprise[-1] = element
print("Обновлённый список surprise:", surprise)

# 10. Создайте англо-французский словарь, который называется e2f, и выведите его на экран.
# Вот ваши первые слова: dog/chien, cat/chat и walrus/morse.
print("Task 10")
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print("Англо-французский словарь:", e2f)

# 11. Используя словарь e2f, выведите французский вариант слова walrus.
print("Task 11")
print(e2f["walrus"])

# 12. Создайте французско-английский словарь f2e на основе словаря e2f. Используйте метод items.
print("Task 12")
f2e = {}
for english_word, french_word in e2f.items():
    f2e[french_word] = english_word
print("Французско-английский словарь:", f2e)

# 13. Используя словарь f2e, выведите английский вариант слова chien.
print("Task 12")
print(f2e["chien"])

# 14. Создайте и выведите на экран множество английских слов из ключей словаря e2f.
print("Task 14")
english_word_set = set(e2f.keys())
print("Множество английских слов:", english_word_set)
# 15. Создайте многоуровневый словарь life. Используйте следующие строки для
# ключей верхнего уровня: 'animals', 'plants' и 'other'. Сделайте так, чтобы ключ
# 'animals' ссылался на другой словарь, имеющий ключи 'cats', 'octopi' и 'emus'.
# Сделайте так, чтобы ключ 'cats' ссылался на список строк со значениями 'Henri',
# 'Grumpy' и 'Lucy'. Остальные ключи должны ссылаться на пустые словари.
print("Task 15")
life = {
    "animals": {
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": {},
        "emus": {},
    },
    "plants": {},
    "other": {},
}
print("Многоуровневый словарь:", life)
# 16. Выведите на экран высокоуровневые ключи словаря life.
print("Task 16")
print("Высокоуровневые ключи:", life.keys())
# 17. Выведите на экран ключи life['animals'].
print("Task 17")
print(life.get("animals").keys())
# 18. Выведите значения life['animals']['cats'].
print("Task 18")
print(life.get("animals").get("cats"))
