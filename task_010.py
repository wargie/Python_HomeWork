import math
def metod_odleglosci(xa, ya, za, xb, yb, zb):
    odleglosc = math.sqrt((xb - xa)**2 + (yb - ya)**2 + (zb - za)**2)
    return odleglosc
xa, ya, za = int(input()), int(input()), int(input())
xb, yb, zb = int(input()), int(input()), int(input())
odleglosc = metod_odleglosci(xa, ya, za, xb, yb, zb)
print(f'Расстояние между точкой A({xa}, {ya}, {za}) и точкой B({xb}, {yb}, {zb}) в пространстве равно {odleglosc}')