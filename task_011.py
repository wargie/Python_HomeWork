#Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
print('Способ первый')
list = []
n = int(input('Введите количество членов последовательности: '))
for i in range(n):
    if i % 2 == 0:
        list.append(3**i)
    else:
        list.append(3**i * -1)
print(list)

print('Способ второй, мой')

n = int(input('Введите количество членов последовательности: '))
def get_degree(n):
    return [((-3)**i) for i in range(n)]
print (get_degree(n))