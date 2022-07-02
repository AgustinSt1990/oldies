from math import*

##CARGA DE VALORES INICIALES
y= float(raw_input('ALTURA INICIAL : '))
if abs(y)<1:
  h=0.00001
if abs(y)>=1 and abs(y)<10:
  h=0.000001
if abs(y)>=10:
  h=0.00000001

lista1= []
lista2= []
lista3= []
y0= 0.0
y0+= y
Dy=0.0 
DDy=9.8*(1-16*y**3)
iteracion= 0
iteracionM= 0
Periodo=0.0
Amplitud=abs(y0)

#MODULO DE CALCULO DE DATOS PREVIOS APROXIMADOS
print '\nPor favor espere 1 min\n'
while (True):
  Dy2=Dy+h*DDy
  y2=y+h*Dy
  DDy=9.8*(1-16*y2**3)
  Dy=Dy2
  y=y2
  iteracion+=1
  Periodo+=h
  if abs(y)<1 and iteracion>10000 and round(y2,2)==round(y0,2):
    Periodo+=h
    break
  if abs(y)>=1 and abs(y)<10 and iteracion>100000 and round(y2,2)==round(y0,2):
    Periodo+=h    
    break
  if abs(y)>=10 and iteracion>1000000 and round(y2,2)==round(y0,2):
    Periodo+=h    
    break

#MODULO DE CARGA DE DATOS
print 'Amplitud max : ', Amplitud, '\nPeriodo [seg] : ', round(Periodo,5)
iteracionM=int(raw_input('n° iteraciones por ciclo deseadas(aprox): '))
print 'paso recomendado (h): ', round(sin(Periodo)/iteracionM,6), '\n',
h=float(raw_input('paso deseado= '))
t=float(raw_input('lapso de tiempo [seg]= '))
iteracionM=round(t/h)

#REINICIAR VALORES
iteracion=0
y= y0
Dy= 0.0
DDy=9.8*(1-16*y**3)
tiempo=h

#PROGRAMA PRINCIPAL
while (iteracion<=iteracionM or tiempo<=t):
  Dy2=Dy+h*DDy
  y2=y+h*Dy
  DDy=9.8*(1-16*y2**3)
  Dy=Dy2
  y=y2
  #MODULO DE ALMACENAMIENTO DE DATOS
  y2= str(y2)
  lista1.append(y2)
  y2= float(y2)
  iteracion=str(iteracion)
  lista2.append(iteracion)
  iteracion=int(iteracion)
  tiempo=str(tiempo)
  lista3.append(tiempo)
  tiempo=float(tiempo)
  #-------------------------------
  print 'y(%d) ='%(iteracion), round(y2,5), ' [%f seg]'%(round(tiempo,5))
  iteracion+=1
  tiempo+=h

#MODULO DE EXPORTACION DE DATOS
raw_input('\nPRESIONE ENTER')
txt = ' '.join(lista1)
iter= ' '.join(lista2)
tiem= ' '.join(lista3)
f = open ('valores.txt', 'w')
g = open ('iteraciones.txt', 'w')
i = open ('tiempo.txt', 'w')
f.write(txt)
g.write(iter)
i.write(tiem)
f.close()
g.close()
i.close()
print 'Datos guardados en valores.txt, iteraciones.txt y tiempo.txt\nGracias por usar el programa'