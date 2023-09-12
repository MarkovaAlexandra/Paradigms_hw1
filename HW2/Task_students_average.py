# Задача 1

# Допустим, у нас есть задача по обработке данных о студентах в университете. У нас есть следующие данные:

# Список студентов с их именами и оценками.
# Нам нужно найти средний балл по всем студентам и вывести имена студентов, чей балл выше среднего.
# Сделать 2 варианта решения , т е Реализация структурного программирования и процедурного программирования

# Список студентов
# Структурное программирование:


student_data = [
 {'name': 'Alice', 'score': 85},
 {'name': 'Bob', 'score': 92},
 {'name': 'Charlie', 'score': 78},
 {'name': 'David', 'score': 95},
 ]

summa = 0                          # вводим переменную для накопления общей суммы баллов
count = 0                          # вводим переменую для подсчета количества студентов

for e in student_data:             # для каждого словаря в списке
    summa += e['score']            # накапливаем сумму
    count +=1                      # считаем студентов

if count != 0:                     # проверка деления на ноль
    average = summa / count        # считаем средний балл
above_average_students = []        # создаем список студентов, у которых балл выше среднего
for e in student_data:             # снова идем по списку
    if e['score'] > average:       # если балл студента выше среднего
        above_average_students.append(e['name'])           # добавляем его в список отличников


print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {above_average_students}")

# Процедурное программирование
def find_average(students):                          # прописываем функцию для нахождения среднего балла и студентов, имеющих балл выше среднего
    summ = 0
    above_average_students = []
    for student in students:
        summ += student['score']
    length = len(students)
    average = summ / length
    for student in students:
        if student['score'] >= average:
            above_average_students.append(student['name'])

    return average, above_average_students                       # возвращаем кортеж из ср балла и списка сутдентов


average1 = find_average(student_data)
print(f"Средний балл: {average1[0]}, студенты с баллом выше среднего: {average1[1]}")
