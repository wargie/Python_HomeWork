#Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('Введённые координаты соответствуют первой четверти')
elif x < 0 and y > 0:
    print('Введённые координаты соответствуют второй четверти')
elif x < 0 and y < 0:
    print('Введённые координаты соответствуют третьей четверти')
elif x > 0 and y < 0:
    print('Введённые координаты соответствуют четвёртой четверти')
elif x == 0:
    print('Точка расположена оси ординат')
elif y == 0:
    print('Точка расположена оси абсцисс')