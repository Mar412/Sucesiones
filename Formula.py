def f1(b, c, d):
    a = (b-1)*(c-d)+d
    return a

y = float(input("inserte primer termino"))
x = float(input("inserte segundo termino"))
n = float(input("Que valor deseas concoer?"))

resultado = f1(n, x, y)
print(resultado)