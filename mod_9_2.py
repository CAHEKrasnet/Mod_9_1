# "Списковые, словарные сборки"
# Даны несколько списков, состоящих из строк
# first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
# second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
# 1. В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings, 
# при условии, что длина строк не менее 5 символов.
# 2. В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины. 
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
# 3. В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки. 
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings. 
# Условие записи пары в словарь - чётная длина строки.


first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1
first_result = [len(x) for x in first_strings if len(x) > 5]
print(first_result)
# 2
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)
# 3
total_strings = first_strings + second_strings
third_result = {x: len(x) for x in total_strings if len(x) % 2 == 0}
print(third_result)


