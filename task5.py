# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.
a = 0
b = 0
c = 1
while c != 0:
    c = int(input())
    n = 0
    while 2**n < (c + 1):
        if c == 2**n:
            a = a+c
            b += 1
        n += 1
if (b == 0):
    print ("Нет")
else:
    print (a/b)