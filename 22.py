# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def fill_array(volume):
    main_list = []
    print(f'Последовательно введите элементы набора чисел, всего {volume}: ')
    for i in range(volume):
        main_list.append(int(input()))
    return main_list

n = int(input('Введите количество элементов первого набора чисел: '))
m = int(input('Введите количество элементов втрого набора чисел: '))
first_collection = set(fill_array(n))
second_collection = set(fill_array(m))
result_collection = first_collection.union(second_collection)
print('Неповторя ющиеся числа из наборов: ')
for i in list(result_collection):
    print(i)
