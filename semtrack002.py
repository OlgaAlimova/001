# 2. Напишите программу, которая на вход принимает 5 чисел и
# находит максимальное из них.
#
# Примеры:
#
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a = int(input('Введите число 1 = '))
b = int(input('Введите число 2 = '))
c = int(input('Введите число 3 = '))
d = int(input('Введите число 4 = '))
e = int(input('Введите число 5 = '))
if a > b:
   if a > c:
       if a > d:
           if a > e:
               print(a)
           else:
               print(e)
       else:
           if d > e:
               print(d)
           else:
               print(e)
   else:
       if c > d:
           if c > e:
               print(c)
           else:
               print(e)
       else:
           if d > e:
               print(d)
           else:
               print(e)
else:
   if b > c:
       if b > d:
           if b > e:
               print(b)
           else:
               print(e)
       else:
           if d > e:
               print(d)
           else:
               print(e)
   else:
       if c > d:
           if c > e:
               print(c)
           else:
               print(e)
       else:
           if d > e:
               print(d)
           else:
               print(e)

numbers = []
for i in range(1, 6):
   numbers.append(int(input(f'Введите {i} число: ')))
max = numbers[0]
for j in range(5):
   if numbers[j] > max:
       max = numbers[j]
print(f'Максимальное число равно: {max}')
