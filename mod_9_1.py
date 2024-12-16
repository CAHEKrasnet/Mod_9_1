# Задача "Вызов разом"
# Запишите функцию apply_all_func(int_list, *functions), которая принимает параметры:

# int_list - список из чисел (int, float)
# *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
# Эта функция должна:

# Вызвать каждую функцию к переданному списку int_list
# Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.

# Пункты задачи:
# 1. В функции apply_all_func создайте пустой словарь results.
# 2. Переберите все функции из *functions.
# 3. При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
# 4. Верните словарь results.
# 5. Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.

# Для того, чтобы взять название функции можно обратиться к атрибуту __name__
# При попытке передачи, например, списка из строк, некоторые функции могут работать некорректно или вовсе не работать. Используйте списки чисел.

def apply_all_func(int_list, *functions):           # 1
    results = {}
    for func in functions:                          # 2
        results[func.__name__] = func(int_list)     # 3

    return results                                  # 4


def min_list(list):
    return min_list(list)


def max_list(list):
    return max_list(list)


def len_list(list):
    return len_list(list)


def sum_list(list):
    total = 0
    for x in list:
        total += x
    return total


def sorted_list(list):
    return sorted_list(list)



print(apply_all_func([6, 20, 15, 9], max, min))                 # 5
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))