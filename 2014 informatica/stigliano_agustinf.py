
from moduloimagen01 import leerIm, dibujarIm, borrarIm
##---------------------PROGRAMA PRINCIPAL--------------------------
print( 'ADVERTENCIA, LUEGO DE UTILIZAR EL FILTRO MITAD DE ALTO, REINICIE EL PROGRAMA.')
mat=leerIm('tux70x78.txt')
a0=[[0]*70]*78
for i in range(len(mat)):
  for j in range(len(mat[0])):
    a0[i][j]=mat[i][j]

id=dibujarIm(mat)

###----------------FILTRO NEGATIVO-----------------

def filtro_1(A):
  
  for i in range(len(A)): #digo que cada elemento sea el numero que hace falta sumarsele para ser 255
    for j in range(len(A[0])):
      if A[i][j]==255:
        A[i][j]=0
      else:
        A[i][j]=255-A[i][j]
      
  id_neg=dibujarIm(A)
  input('Presione return para continuar\n')
  clc=borrarIm(id_neg)
  for i in range(len(a0)):
    for j in range(len(a0[0])):
      mat[i][j]=a0[i][j]
  return

###---------------FILTRO ROTACION ANTIHORARIO------------------

def filtro_2(B):

  for i in range(len(B)): #invierto el orden de los elementos de cada fila
    for j in range(len(B[0])/2):
      c=B[i][j]
      B[i][j]=B[i][len(B[0])-1-j]
      B[i][len(B[0])-1-j]=c


  c=[] #creo matriz auxiliar
  m=len(B[0])
  n=len(B)
  for f in range(m):
    c.append([0]*n)
  
  for i in range(len(B)): #calculo su transpuesta
    for j in range(len(B[0])):
      c[j][i]=B[i][j]
    
  B=c #igualo matrices
  id_antihor=dibujarIm(B)
  input('Presione return para continuar\n')
  clc=borrarIm(id_antihor)
  for i in range(len(a0)):
    for j in range(len(a0[0])):
      mat[i][j]=a0[i][j]
  return

###-------------------FILTRO LA MITAD DE ALTO--------------

def filtro_3(C):

  for i in range(len(C)/2):#invertir el orden de las filas
    c=C[i]
    C[i]=C[len(C)-1-i]
    C[len(C)-1-i]=c

  c=[255]*len(C[0]) #creo una matriz auxiliar
  m=len(C)/2
  for i in range(m): #inserto la matriz auxiliar en el final de la matriz invertida
    C.append(c)

  for i in range(len(C)/2): #vuelvo a invertir el orden de las filas
    c=C[i]
    C[i]=C[len(C)-1-i]
    C[len(C)-1-i]=c
  c=[255]*len(C[0])
  for i in range(m): #inserto la matriz auxiliar en el final de la matriz modificada
    C.append(c)
  id_alto=dibujarIm(C)
  input('Presione return para continuar\n')
  clc=borrarIm(id_alto)
  
  for i in range(len(a0)):
    for j in range(len(a0[0])):
      mat[i][j]=a0[i][j]
  return
###---------------------MENU---------------------


def menu():
    mensage = """Escoja algun de las siguientes opciones:
    a) Filtro de Color Negativo
    b) Filtro de Rotaci�n Antihoraria
    c) Filtro de Mitad de Alto
    d) Cerrar el Programa

    Opcion: """
   
    while True:

      op = input(mensage)
      if op == 'a':
        filtro_1(mat)
      elif op == 'b':
        filtro_2(mat)
      elif op == 'c':
        filtro_3(mat)
      elif op == 'd':
        print( '\nGracias por usar el Programa')
        clc=borrarIm(id)
        break
      else:
        print( '\nOpcion no valida\n')

menu()