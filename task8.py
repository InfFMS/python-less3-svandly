# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить, сколько было введено положительных и
# сколько отрицательных чисел (нули не считать!).
a = int(input())
c = 0
b = 0
d = 1
e = 0
while e < a:
    c = int(input())
    if c < 0:
        b += 1
    elif c > 0:
        d += 1
e+=1
print ('Положительных чисел', d, 'отрицательных чисел', b)