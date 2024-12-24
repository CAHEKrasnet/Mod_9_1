# Домашнее задание по теме "Декораторы"

"""
Напишите 2 функции:
1. Функция, которая складывает 3 числа (sum_three)
2.Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
 1. Функция is_prime должна возвращать wrapper
 2. @is_prime - декоратор для функции sum_three
"""



def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        
        if result < 2:
            print(f"Не простое и не сложное число\n{result}")
        elif result == 2:
            print(f"Простое\n{result}")
        elif result > 2:
            if all((result % i != 0) for i in range(2, int(result ** 0.5) + 1)):
                print(f"Простое\n{result}")
            else:
                print(f"Составное\n{result}")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c
    


res = sum_three(2, 3, 6)
res = sum_three(45, 34, 1111)
res = sum_three(-5, 4, 0)
