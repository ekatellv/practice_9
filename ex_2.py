from math import sqrt
n = int(input('введите число: '))
while n <= 2:
    print('неверное значение')
    n = int(input('введите число: '))
while n > 2:
    n = sqrt(n)
    print(f'{n:.3f}')
