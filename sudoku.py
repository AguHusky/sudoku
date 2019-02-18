#from numpy import arange
# Declaracion de variables para matriz
a0=[]; a1 = []; a2 = []; a3 = []; a4=[]; a5=[]; a6=2; a7=[]; a8=[] 
b0=5; b1 = []; b2 = []; b3 = []; b4=[]; b5=4; b6=[]; b7=3; b8=[] 
c0=8; c1 = []; c2 = []; c3 = 7; c4=[]; c5=[]; c6=6; c7=5; c8=[]
d0=[]; d1 = []; d2 = []; d3 = 5; d4=3; d5=[]; d6=[]; d7=7; d8=[]
e0=[]; e1 = 8; e2 = []; e3 = []; e4=[]; e5=[]; e6=[]; e7=1; e8=[]
f0=[]; f1 = 6; f2 = []; f3 = []; f4=4; f5=2; f6=[]; f7=[]; f8=[]
g0=[]; g1 = 5; g2 = 6; g3 = []; g4=[]; g5=2; g6=[]; g7=[]; g8=1
h0=[]; h1 = 2; h2 = []; h3 = 8; h4=[]; h5=[]; h6=[]; h7=[]; h8=7
i0=[]; i1 = []; i2 = 9; i3 = []; i4=[]; i5=[]; i6=[]; i7=[]; i8=[]       
n1=1; n2=2; n3=3; n4=4; n5=5; n6=6; n7=7; n8=8; n9=9
# Declaracion de Filas
A = a0, a1, a2, a3, a4, a5, a6, a7, a8, b0, b1, b2, b3, b4, b5, b6, b7, b8, c0, c1, c2, c3, c4, c5, c6, c7 ,c8, d0, d1, d2, d3, d4, d5, d6, d7, d8, e0, e1, e2, e3, e4, e5, e6, e7, e8, f0, f1, f2, f3, f4, f5, f6, f7, f8, g0, g1, g2, g3, g4, g5, g6, g7, g8, h0, h1, h2, h3, h4, h5, h6, h7, h8, i0, i1, i2, i3, i4, i5, i6, i7, i8
num=n1, n2, n3, n4, n5, n6, n7, n8, n9

#Archivo sudoku.txt
with open("sudoku.txt", "w") as sudoku_file:
    #Array para guardar numeros que pueden estar en la posicion
    arrayV=[]
    #Cantidad de cuadros
    n=81
    #Numeros posibles en num
    m=9
    #Loop para comparacion de posiciones en el cuadro
    h=0
    while h<n:
        d=0
        while d<m:
            #Si el numero de A[h] es diferente al numero num[d]
            if A[h] != num[d]:
                #Guarda el numero en la lista de numeros posibles arrayV
                arrayV.append(num[d])
            d+=1
            #Checar si la posicion tiene un numero por default
            count=0
            for x in arrayV:
                count+=1
        print(str(count))
        #Solo se guardan los numeros posibles de las casillas vacias
        if(count==m):       
        #Guardar la lista en el archivo sudoku.txt
            output='Posicion de A'+str(h)
            output+= "\n "
            output+=str(arrayV)
            output+="\n"
            sudoku_file.write(output)
              #Limpiar el arrayV
        arrayV[:]=[]
        
        h+=1
        
        
        

