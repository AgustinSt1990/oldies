### PROGRAMA PARA CALCULAR LOS MODOS Y FRECUENCIAS MEDIANTE EL METODO DE STODOLA
#
# 1. ESPACIO RESERVADO PARA EL MENU


# 2. CARGAR FUNCIONES 
def COPIAR_MATRIZ_(M):
  X = []
  for i in range(len(M)):
    for j in range(len(M[0])):
      a = M[i][j]
      X.append([a])
  return X

def NORMALIZACION_(M):
  X = COPIAR_MATRIZ_(M)
  aux = []
  for i in range (len(M)-1):
    if abs(M[i][0]) > abs(M[i+1][0]):
      aux = (M[i][0])
      M[i][0]= M[i+1][0]
      M[i+1][0]=aux
  A = M[-1][0]
  for i in range (len(M)): 
    X[i][0]/=A    
  return X

def MATRIZ_TRANSPUESTA_(A):
  X = []
  Y = []
  for i in range (len(A)):
    Y.append(A[i][0])
  X.append(Y)
  return X
      
def COEFICIENTE_MODAL_(V, A, U):
  X = MATRIZ_TRANSPUESTA_(V)
  F1_ = PRODUCTO_MATRIZ_(X,A)
  F2_ = PRODUCTO_MATRIZ_(F1_,U)
  F3_ = PRODUCTO_MATRIZ_(F1_,V)
  a = F2_[0][0]/F3_[0][0]
  return a

def FILTRADO_ (A,B,q):
  X = VECTOR_(len(A))
  for i in range(len(A)):
    X[i][0]= A[i][0] - q * B[i][0]
  return X

def MATRIZ_(d):
  X=[]
  for i in range(d):
    X.append([0]*d)
  return X

def MATRIZ_2_(m,n):
  X=[]
  for i in range(m):
    X.append([0]*n)
  return X

def VECTOR_(d):
  X = []
  for i in range (d):
    X.append([1])
  return X

def MATRIZ_COMPLETA_(M): ## CORREJIR FORMATO DE IMPRESION
  for i in range (len(M)):
    for j in range (len(M[0])):
      print ('\nElemento ', [i+1], [j+1])
      M[i][j]= float(input('>> '))
  return M

def MATRIZ_SIMETRICA_(M): ## CORREJIR FORMATO DE IMPRESION
  for i in range (len(M)):
    for j in range (len(M[0])):
      if i==j or i<j:
        print ('\nElemento ', [i+1], [j+1])
        M[i][j]= float(input('>> '))
      if i>j:
        M[i][j] = M[j][i]
  return M

def MATRIZ_DIAGONAL_(M):
  for i in range (len(M)):
    for j in range (len(M[0])):
      if i==j:
        print ('--- [M] ---\nElemento ', [i+1], [j+1])
        M[i][j]= float(input('>> '))
  return M

def PRODUCTO_MATRIZ_(A,B):  ## OBS: A[i][k]*B[k][l] = R [i][l]
  R=[]
  R = MATRIZ_2_(len(A),len(B[0]))
  sum = 0.0
  for i in range (len(A)):
    for l in range (len(B[0])):
      for k in range (len(A[0])):
        sum += A[i][k]*B[k][l]
      R[i][l] = sum
      sum = 0.0
  return R
    
# 3. PROGRAMA PRINCIPAL: 
##ADVERTENCIA!! [F] Y [M] ESTAN CARGADOS A MANO

d = int(input('dimension de la matriz de flexibilidad: '))
#F = MATRIZ_(d)
#M = MATRIZ_(d)
#F = MATRIZ_COMPLETA_(F)
#M = MATRIZ_DIAGONAL_(M)
############################## CARGA MANUAL DE F Y M - TEMPORAL
F = [[6.671e-4 , -8.571e-6 , 3.581e-5] , [-8.571e-6 , 1.428e-7 , -3.571e-7] , [3.571e-5 , -3.571e-7 , 1.042e-5]]
M = [[10 , 0 , 0] , [0 , 100 , 0] , [0 , 0 , 10]]
FM = PRODUCTO_MATRIZ_(F,M)
U_0 = VECTOR_(d)

# 3.1 APLICACION DEL METODO DE STODOLA

# 3.1.1 PRIMER MODO
U_1 = PRODUCTO_MATRIZ_(FM,U_0)
for i in range (5): #numero arbitrario de iteraciones: 5
  U_1 = NORMALIZACION_(U_1)
  aux = U_1[0][0]
  U_1 = PRODUCTO_MATRIZ_(FM,U_1)
  w_1 = aux/U_1[0][0]
phi_1 = NORMALIZACION_(U_1)

print ('\ncolumna phi_1: \n',phi_1[0],'\n', phi_1[1],'\n', phi_1[2], '\n\nfrecuencia asociada\nw1^2 = ', w_1 ,'\nFIN MODO 1')

# 3.1.2 SEGUNDO MODO
q_1 = COEFICIENTE_MODAL_(phi_1, M, U_0)
U_2 = FILTRADO_(U_0,phi_1,q_1)
U_2 = NORMALIZACION_(U_2)
for i in range(6):
  U_2 = PRODUCTO_MATRIZ_(FM,U_2)
  U_2 = NORMALIZACION_(U_2)
  q_2 = COEFICIENTE_MODAL_(phi_1, M, U_2)
  U_2 = FILTRADO_(U_2, phi_1, q_2)
  U_2 = NORMALIZACION_(U_2)
phi_2 = COPIAR_MATRIZ_(U_2)  
U_2 = PRODUCTO_MATRIZ_(FM,U_2)
aux = U_2[2][0]

w_2 = phi_2[2][0]/aux

print ('\ncolumna phi_2: \n',phi_2[0],'\n', phi_2[1],'\n', phi_2[2], '\n\nfrecuencia asociada\nw2^2 = ', w_2 ,'\nFIN MODO 2')

# 3.1.3 TERCER MODO
q_2 = COEFICIENTE_MODAL_(phi_2, M, U_0)
U_3 = FILTRADO_(U_0, phi_1, q_1)
U_3 = FILTRADO_(U_3, phi_2, q_2)
U_3 = NORMALIZACION_(U_3)
##print ('\n U_3 = ', U_3, '\n')
phi_3 = COPIAR_MATRIZ_(U_3)
aux = U_3[1][0]
U_3 = PRODUCTO_MATRIZ_(FM,U_3)
w_3 = aux/U_3[1][0]


print ('\ncolumna phi_3: \n',phi_3[0],'\n', phi_3[1],'\n', phi_3[2], '\n\nfrecuencia asociada\nw3^2 = ', w_3 ,'\nFIN MODO 3')


































##print (U_0, '\n (i,j) =','(', len(U_0), ',', len(U_0[0]), ')' ### PRINT QUE PERMITE VER LA DIMENSION DE LA MATRIZ FACILMENTE)
##print ('\n', FM[0], '\n', FM[1], '\n', FM[2]  ##el print solo funciona para matriz 3x3 PERO VIZUALIZA LA MATRIZ EN FORMATO CORRECTO)
