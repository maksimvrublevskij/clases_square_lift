from Elevator_elevator import Elevator

class NewElevator(Elevator):
    def __init__(self, total_floors=int(input('Сколько этажей в доме: ')), current_floor=int(input('На каком этаже находится лифт: '))):
        super().__init__(total_floors, current_floor)

    def buttons(self):
        super().buttons()

    def move(self):
        if n == 'move':
            a = int(input('введите номер этажа: '))
            if a < self.total_floors:
                print(f'Лифт отправляется с {self.current_floor} этажа на {a} этаж')
            else:
                print('Неправильный номер этажа')
        else:
            super().buttons()


elevator = NewElevator()
n = input('Нажмите (up) или (down) или (move) в зависимости (вверх) или (вниз) или (на указанный этаж) Вам надо: ')
elevator.buttons()
elevator.move()