#Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
import random
quarter = random.randint(1, 4)
print(f'Сгенерирован случайный номер четверти = {quarter}')
#quarter = int(input())
if quarter == 1:
    zakres = "x > 0, y > 0"
elif quarter == 2:
    zakres = "x < 0, y > 0"
elif quarter == 3:
    zakres = "x < 0, y < 0"
elif quarter == 4:
    zakres = "x > 0, y < 0"
print(f'Для {quarter}-й четверти координаты точки должны быть заданы в диапазоне ({zakres})')