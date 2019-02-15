# Declaracion de variables para matriz
a0 = 2; a1 = 3; a2 = 1; a3 = 4
b0 = 4; b1 = 1; b2 = 3; b3 = 2
c0 = 3; c1 = 2; c2 = 4; c3 = 1
d0 = 1; d1 = 4; d2 = 2; d3 = 3
# Declaracion de Filas
A = a0, a1, a2, a3
B = b0, b1, b2, b3
C = c0, c1, c2, c3
D = d0, d1, d2, d3
# Impresion de Filas
print(A)
print(B)
print(C)
print(D)
# Comparando
if a0 == a1:
    print(str(a0) +' es igual a ' + str(a1))
elif a0 == a2:
    print(str(a0) +' es igual ' + str(a2))
elif a0 == a3:
    print(str(a0) +' es igual ' + str(a3))
elif a0 == b0:
    print(str(a0) +' es igual ' + str(b0))
elif a0 == c0:
    print(str(a0) +' es igual ' + str(c0))
elif a0 == d0:
    print(str(a0) +' es igual ' + str(d0))
else:
    print(str(a0) +' esta bien en posicion a0')
