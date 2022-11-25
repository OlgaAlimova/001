# Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

x = int(input('Введите значение X: '))
y = int(input('Введите значение Y: '))
z = int(input('Введите значение Z: '))

result = not (x or y or z)
res = (not x) and (not y) and (not z)
# print(x, y, z)
# print(result, res)
if result == res:
   print('Утверждение истинно')
else:
   print('Утверждение ложно')