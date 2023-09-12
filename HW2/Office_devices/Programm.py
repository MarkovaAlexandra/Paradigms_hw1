# Мы хотим выполнить следующие операции:
# __
# Добавить новое устройство в комнату.
# Включить или выключить устройство в комнате.
# Поиск устройства по типу и статусу.
# Получить список всех устройств в конкретной комнате.
# Подсчитать общее количество устройств каждого типа в офисе.

from Office import *
from Device import *
from Room import *

# Создаем новые устройства
device1001 = Device('computer', 'on', 1001)
device1002 = Device('lamp', 'off', 1002)
device1003 = Device('printer', 'on', 1003)
device1004 = Device('lamp', 'off', 1004)
device1005 = Device('printer', 'on', 1005)
device1006 = Device('computer', 'on', 1006)
device1007 = Device('computer', 'on', 1007)
device1008 = Device('lamp', 'off', 1008)


# Создаем новый офис
office = Office('myoffice')

# Создаем новые комнаты
room321 = Room(321)
room123 = Room(123)

# Добавляем комнаты в офис
office.add_room(room321)
office.add_room(room123)

# Добавляем устройства в комнаты
room321.add_device(device1001)
room321.add_device(device1002)
room321.add_device(device1003)
room321.add_device(device1004)
room321.add_device(device1005)

room123.add_device(device1006)
room123.add_device(device1007)
room123.add_device(device1008)

# Список устройств в комнате
print('room 321')
room321.show_all_devices()
print("______________")

# Список устройст в комнате
print("room123")
room123.show_all_devices()
print("______________")

# Список устройст во всем офисе
print("office")
office.show_office_devices()

# Поиск устройст по типу и статусу в комнате
print('включенные компьютеры в 321 комнате')
room321.find_device_by_type_and_status('computer', 'on')

# Поиск устройств по типу и статусу в офисе
print('включенные компьютеры в офисе')
office.find_devices_by_type_and_status_oficce('computer', 'on')

# Переключение статуса устройства
room123.turn_device_in_room(1007)
print('выключаем 1007 копьютер')
# Проверка (еще раз выводим устройства по типу и статусу, ожидаем вывод без устройства 1007
print('включенные компьютеры в офисе')
office.find_devices_by_type_and_status_oficce('computer', 'on')

# Подсчет количества устройств в комнате по типу
print('сколько ламп в 321 комнате')
print(room321.count_devices_by_type('lamp'))

#  Подсчет количества устройст в офисе по типу
print('сколько ламп в офисе')
print(office.count_devices_by_type_office('lamp'))