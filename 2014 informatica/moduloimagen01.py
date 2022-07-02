# -*- coding: iso-8859-15 -*-
#
# VERSION 1.1 (5-Noviembre-2003)
#
# AYUDA del m�dulo 'moduloimagen'. Define tres funciones, 
# que podemos utilizar de la siguiente forma:
#
# - matriz = leerIm(nombreFichero). Lee la imagen del fichero
#   indicado y la devuelve como una matriz de enteros. Cada 
#   elemento de la matriz se corresponde con un pixel de la 
#   imagen. 
#
# - id = dibujarIm(matriz). Se dibuja la imagen en la ventana 
#   gr�fica. La imagen se escala autom�ticamente para ocupar toda
#   la ventana gr�fica. El valor devuelto por la funci�n puede 
#   utilizarse para borrar la imagen con la funci�n que se presenta
#   a continuaci�n.
#
# - borrarImagen(id). Borra la imagen identificada como 'id'.
#

def _entero2color(n):
  return '#'+('%02x'%n)*3

def leerIm(nombreFichero):
  #lee imagen del fichero tux.txt
  f=open(nombreFichero)
  im1=f.read()
  f.close()
  #convierte datos en matriz
  lin=im1.split('\n')
  mat=[]
  for l in lin:
    if l=='': break
    
    mat.append(list(map(int,l.split())))
  return mat

def dibujarIm(mat):
  filas=len(mat)
  columnas=len(mat[0])
  l=[]
  xx1,yy1,xx2,yy2=window_coordinates()
  
  px=float(xx2-xx1)/columnas
  py=float(yy2-yy1)/filas
  for i in range(filas):
    for j in range(columnas):
      if mat[i][j]==-1: 
        col='#ffff00'
      else:
        col=_entero2color(mat[i][j])
      x1=xx1+px*j
      y1=yy2-py*(i+1)
      x2=xx1+px*(j+1)
      y2=yy2-py*i
      l.append(create_filled_rectangle(x1,y1,x2,y2,col))
  return l

def borrarIm(ind):
  map(erase,ind)
