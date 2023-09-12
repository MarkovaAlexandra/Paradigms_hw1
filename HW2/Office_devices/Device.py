# Класс Устройство

class Device():
    def __init__(self, type, status, id):    #конструктор класса
        self._type = type
        self._status = status
        self._id = id

    @property
    def type(self):
        return self._type
    @property
    def status(self):
        return self._status

    @property
    def id(self):
        return self._id

    @type.setter
    def type(self, new_type):
        self._type = new_type


    def change_status(self):                        # функция изменения статуса(вкл.выкл)
        if self._status == 'on':                    # если статус вкл - меняем на выкл
            self._status = 'off'
        else:self._status = 'on'                    # элсе меняем на вкл



    def __str__(self) -> str:                       # ту стринг (красиво распечатать устройство)
        return f"{self._type} {self._status} {self._id} "