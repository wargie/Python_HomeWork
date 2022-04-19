#Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
import random
quarter = random.randint(1, 4)
print(f'Сгенерирован случайный номер четверти равный {quarter}')
if quarter == 1:
    zakres = "x > 0, y > 0"
elif quarter == 2:
    zakres = "x < 0, y > 0"
elif quarter == 3:
    zakres = "x < 0, y < 0"
elif quarter == 4:
    zakres = "x > 0, y < 0"
print(f'Для {quarter}-й четверти координаты точки лежат в диапазоне в диапазоне ({zakres})')