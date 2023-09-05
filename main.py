def sort_list_imperative(numbers):
    for j in range(0, len(numbers) - 1):
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers


def sort_list_declarative(numbers):
    return sorted(numbers)


mylist = [5, 2, 9, 4, 1, 3]
mylist1 = [5, 2, 9, 4, 1, 3]
print("Сортировка императивным методом")
print(sort_list_imperative(mylist))
print('________________________________')
print("Сортировка декларативным методом")
print(sort_list_declarative(mylist1))
print('________________________________')


# Задача- 1: У вас есть массив целых чисел, в котором каждое число, кроме одного,
# повторяется дважды. Вам нужно найти это одиночное число.

# Пример:
# Входной массив: [4, 3, 2, 4, 1, 3, 2]
# Результат: 1
# В данной задаче вы должны найти способ найти одиночное число с использованием массивов и алгоритмов.

def find_single(numbers):
    mynumbers = sorted(numbers)
    i = 0
    while i < len(mynumbers) - 1:
        if mynumbers[i] == mynumbers[i + 1]:
            i += 2
            if i == len(mynumbers) - 1:
                return mynumbers[i]
        else:
            return mynumbers[i]


mylist2 = [4, 3, 2, 3, 1, 1, 2]
print(mylist2)
print(f'одиночное число: {find_single(mylist2)}')
print('________________________________')


# Задача-2: У вас есть массив, содержащий числа от 1 до N, где N - длина массива.
# Одно из чисел в массиве повторяется дважды, а одно число пропущено.
# Найдите повторяющееся число и пропущенное число.

# Пример:
# Входной массив: [2, 3, 1, 5, 3]
# Повторяющееся число: 3
# Пропущенное число: 4

def find_missed_and_double(numbers):
    mynumbers = sorted(numbers)
    for i in range(0, len(mynumbers) - 1):
        if mynumbers[i] == mynumbers[i + 1]:
            mydouble = mynumbers[i]
        if mynumbers[i] == mynumbers[i + 1] - 2:
            mymissed = mynumbers[i] + 1
    return mydouble, mymissed


mylist3 = [2, 4, 1, 3, 6, 1]
print(mylist3)
num_double, num_missed = find_missed_and_double(mylist3)
print(f'повторяющееся число: {num_double}')
print(f'пропущенное число: {num_missed}')
