# Домашнее задание по теме "Генераторы"

# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

# Пункты задачи:
# 1 Напишите функцию-генератор all_variants(text).
# 2 Опишите логику работы внутри функции all_variants.
# 3 Вызовите функцию all_variants и выполните итерации.

# Примечания:
# Для функции генератора используйте оператор yield.

def all_variants(text):
    n = len(text)
    for r in range(1, n + 1):                   # Проходим по строке циклом, равным количеству символов
        for j in range(n - r + 1):              # Вложенный цикл для изменения точек начала и конца среза
            yield text[j:j + r]                 # Помещаем в yield сорез строки


a = all_variants("abc")
for i in a:
    print(i)


