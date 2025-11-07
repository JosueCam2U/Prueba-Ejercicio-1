def dimension(matriz):
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0
    return filas, columnas

def inicializar(nf, nc):
    A = []
    for i in range(nf):
        fila = [0] * nc
        A.append(fila)
    return A

def imprimir (A):
    f, c = dimension (A)
    for i in range (0,f):
        print ("| ", end = "") 
        for j in range (0,c):
            print ("{:>5} |".format(A[i][j]), end = "")
        print('')

def shiftRows (mensaje):
    filas,columnas = dimension (mensaje)
    reciba = inicializar (filas,columnas)
    for i in range(filas):
        for j in range(columnas):
            nuevo = (i + j) % columnas
            reciba[i][j] = mensaje [i][nuevo]
    return reciba


mensaje = [[0.0,0.1,0.2,0.3],
           [1.0,1.1,1.2,1.3],
           [2.0,2.1,2.2,2.3],
           [3.0,3.1,3.2,3.3],]

print("---------------------------")
imprimir(mensaje)
print("---------------------------")
imprimir(shiftRows(mensaje))