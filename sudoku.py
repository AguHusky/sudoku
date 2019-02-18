#from numpy import arange
# Declaracion de variables para matriz
a0=[]; a1 = 3; a2 = 1; a3 = []
b0 = 4; b1 = []; b2 = 3; b3 = 2
c0 = []; c1 = 2; c2 = []; c3 = 1
d0 = 1; d1 = []; d2 = 2; d3 = []
n1=1; n2=2; n3=3; n4=4
# Declaracion de Filas
A = a0, a1, a2, a3
B = b0, b1, b2, b3
C = c0, c1, c2, c3
D = d0, d1, d2, d3
num=n1, n2, n3, n4
#num=arange(1,5)
# Impresion de Filas
#print(A)
#print(B)
#print(C)
#print(D)
# Comparando
#if a0 == a1:
 #   print(str(a0) +' es igual a ' + str(a1))
#elif a0 == a2:
 #   print(str(a0) +' es igual ' + str(a2))
#elif a0 == a3:
 #   print(str(a0) +' es igual ' + str(a3))
#elif a0 == b0:
 #   print(str(a0) +' es igual ' + str(b0))
#elif a0 == c0:
 #   print(str(a0) +' es igual ' + str(c0))
#elif a0 == d0:
 #   print(str(a0) +' es igual ' + str(d0))
#else:
 #   print(str(a0) +' esta bien en posicion a0')
    

#i=0
#while i<4:
 #   j=0
  #  while j<4:
   #     print(A[i])
    #    print(B[j])
     #   j+=1
    #i+=1

#Archivo sudoku.txt
with open("sudoku.txt", "w") as sudoku_file:
    #Array para guardar numeros que pueden estar en la posicion
    arrayV=[]
    #Loop para comparacion de posiciones
    h=0
    while h<4:
        d=0
        while d<4:
            #Si el numero de A[h] es diferente al numero num[d]
            if A[h] != num[d]:
                #Guarda el numero en la lista de numeros posibles arrayV
                arrayV.append(num[d])
            d+=1
        #Guardar la lista en el archivo sudoku.txt
        output='Posicion de A'+str(h)
        output+= "\n "
        output+=str(arrayV)
        output+="\n"
        sudoku_file.write(output)
        #Limpiar el arrayV
        arrayV[:]=[]
        h+=1

