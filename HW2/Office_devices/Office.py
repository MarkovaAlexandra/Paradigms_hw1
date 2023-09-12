class Office():
    def __init__(self, name):                      # конструктор класса
        self._name = name
        list = []
        self._list = list

    # Метод для добавления комнат
    def add_room(self, room):
        self._list.append(room)

    # Метод для вывода всех устройст офиса
    # для каждой комнаты вызывается метод вывода всех устройств
    def show_office_devices(self):
        for room in self._list:
            room.show_all_devices()

    # Метод поиска устройств по типу и статусу (для каждой комнаты вызывается соответствующий метод)
    def find_devices_by_type_and_status_oficce(self, type, status):
        for room in self._list:
            room.find_device_by_type_and_status(type, status)

    # Метод подсчета всех устройств в офисе по типу (для каждой комнаты вызывается соответствующий метод)
    def count_devices_by_type_office(self, type):
        count = 0
        for room in self._list:
            count += room.count_devices_by_type(type)
        return count