#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
a = 0
b = 0
c = 1
while (c > 0) or (c < 0):
    c = int(input())
    if c > 0:
        a += 1
    elif c < 0:
        b += 1
print ('Положительных чисел',a ,'отрицательных чисел', b)