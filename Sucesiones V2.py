def f1(x, y):
    new_x = (y - x)
    return new_x

a = float(input("Primer Numero de tu sucesion: "))
b = float(input("Segundo Numero de tu sucesion: "))
d = float(input("Para que termino necesitas la formula: "))

if d > 2:
    numero_siguiente = float(input("que numero desea que sea el {}: ".format(d)))
else:
    numero_siguiente = int(2)
j = f1(a, b)
k = a

j_string = str(j)
a_string = str(a)

def f2(n):
    new_n = (n - 1)
    return new_n
g = f2(d)
h = g * j
l = h + k
valor = numero_siguiente - l
def f3(b):
    new_b = (b - 1)
    new2_b = (b - 2)
    new3_b = (new_b * new2_b)
    return new3_b

try:
    total = valor / f3(d)
except ZeroDivisionError:
    total = int(0)
    file = open("demo.txt", 'w')
    file.write("Bn = ")
    file.write("(n-1)")
    file.write(j_string)
    file.write("+")
    file.write(a_string)
    file.close()

    file = open("demo.txt", 'r')
    print(file.read())
    file.close()

if total != 0:
    total2 = str(total)

    file = open("demo.txt", 'w')
    file.write("Bn = ")
    file.write(total2)
    file.write("(n-1)(n-2) +")
    file.write("(n-1)")
    file.write(j_string)
    file.write("+")
    file.write(a_string)
    file.close()

    file = open("demo.txt", 'r')
    print(file.read())
    file.close()
    print("Toma tu formaula para 3 digitos perro")
else:
    print("Toma tu formula perro, para dos digitos")