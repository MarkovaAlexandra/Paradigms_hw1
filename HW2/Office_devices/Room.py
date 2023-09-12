class Room():
    def __init__(self, room_number):                              # конструктор
        self._room_number = room_number
        list =[]
        self._list = list

    # метод добавления устройства в комнату
    def add_device(self, device):
        self._list.append(device)

    # метод поиска устройства  в комнате по типу и статусу
    def find_device_by_type_and_status(self, type, status):
        for device in self._list:
            if device.status==status and device.type == type:
                print(device)

    # метод для вывода всех устройств в комнате
    def show_all_devices(self):
         for device in self._list:
             print(device)

    #метод для переключения статуса устройства (вкл.выкл)
    def turn_device_in_room(self,id):
        for device in self._list:
            if device.id == id:             # если id устройства совпадает с заданным
                device.change_status()      # то у найденного устройства вызывается метов переключения статуса

    # Метод для подсчета устройств в комнате по типу
    def count_devices_by_type(self, type):
        count = 0                           # переменная для подсчета устройств
        for device in self._list:
            if device.type == type:
                count +=1
        return count