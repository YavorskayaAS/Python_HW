# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = bool
y = bool
z = bool

a = x or y or z
a = not a

b = not x and not y and not z

if a == b :
    print('True')
else :
    print('False')