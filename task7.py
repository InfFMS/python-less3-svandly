# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное из введённых чисел Фибоначчи.
# Вывести "нет", если чисел Фибоначчи в последовательности нет.
# Числа Фибоначчи – это последовательность чисел,
# которая начинается с двух единиц и каждое следующее число
# равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …
a = 1
b = 1
min = 10**9
f = int(input())
c = 0
while f != 0:
    while c < (f + 1):
        c = a + b
        if (a < b):
            a = c
        else:
            b = c
    if (a == f) or (b == f):
        if f < min:
            min = f
    f = int(input())
    c = 0
    a = 1
    b = 1
if (min == 10 ** 9):
    print("Нет")
else:
    print('Минимальное значение', min)

