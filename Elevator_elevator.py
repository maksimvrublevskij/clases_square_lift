class Elevator:
  def __init__(self, total_floors=int(input('Сколько этажей в доме: ')), current_floor=int(input('На каком этаже находится лифт: '))):
    self.total_floors = total_floors
    self.current_floor = current_floor
    print('-----------------')
    print(f'Лифт установлен в доме {self.total_floors} этажей\n'
            f'находится на {self.current_floor} этаже')
    print('-----------------')


  def buttons(self):
    if n == 'up':
      if self.current_floor < self.total_floors:
        self.current_floor += 1
        print(f'Лифт поднимется на {self.current_floor} этаж.')
      else:
        print('Вы находитесь на верхнем этаже.')
    if n == 'down':
      if self.current_floor > 1:
        self.current_floor -= 1
        print(f'Лифт опустится на {self.current_floor} этаж.')
      else:
        print('Вы находитесь на нижнем этаже.')


elevator = Elevator()
n = input('Нажмите (up) или (down) в зависимости (вверх) или (вниз) Вам надо: ')
elevator.buttons()