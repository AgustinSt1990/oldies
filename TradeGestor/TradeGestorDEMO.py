import os
import datetime as dt
print("---------------------------------------\nBienvenidos a Trader Gestor Version DEMO\n---------------------------------------")
print("Manual de usuario en Youtube. Canal: Jackone action software")
def menu():
  msj = """\n\n\t>                <
\t> MENU PRINCIPAL <
\t>                <
\nElija una opcion:
    1) Cuentas
    2) Operaciones
    3) Notas
    4) Configuracion
    0) Salir\n"""
  opcion = check_opcion2_str(msj,4)
  return opcion

def menu1():
  msj = """\n\n\t> MENU CUENTAS <
\nElija una opcion:
    1) Crear cuenta
    2) Registro de cuentas
    3) Actualizar cuenta
    4) Cargar cuentas
    0) Volver\n"""
  opcion = check_opcion2_str(msj,4)
  return opcion

def crearcuenta():
  nombre = raw_input('\nIngrese nombre de la cuenta: ')
  nombre = nombre.lower()
  archivo1 = open(nombre+'.user','w')
  registro(nombre)
  dinCta = float(raw_input('Dinero en cuenta = '))
  riskCta = int(raw_input('Riesgo cuenta [%] = '))
  perdidasacep = dinCta * riskCta/100
  print('Unidad de riesgo = ',perdidasacep,'[usd]\n')
  archivo1.write(str(dinCta)+'\n')
  archivo1.write(str(riskCta)+'\n')
  archivo1.write(str(perdidasacep)+'\n')
  archivo1.close()
  copiarcuenta(dinCta,riskCta,perdidasacep,nombre)
  print("Cuenta guardada\n")
  return dinCta,riskCta,perdidasacep
def crearcuenta2():
  nombre = raw_input('Ingrese nombre de la cuenta: ')
  nombre = nombre.lower()
  cargarcuenta3(nombre)
  if existe_archivo(nombre+'.user'):
    archivo1 = open(nombre+'.user','w')
    dinCta = float(raw_input('Dinero en cuenta = '))
    riskCta = int(raw_input('Riesgo cuenta [%] = '))
    perdidasacep = dinCta * riskCta/100
    print('Unidad de riesgo = ',perdidasacep,'[usd]\n')
    archivo1.write(str(dinCta)+'\n')
    archivo1.write(str(riskCta)+'\n')
    archivo1.write(str(perdidasacep)+'\n')
    archivo1.close()
    copiarcuenta(dinCta,riskCta,perdidasacep,nombre)
    print("Cuenta guardada\n")
    return dinCta,riskCta,perdidasacep
  else:
    return False,False,False
def copiarcuenta(a,b,c,d):
  archivo1 = open('E_cuentatradergestor.txt','w')
  archivo1.write(str(a)+'\n')
  archivo1.write(str(b)+'\n')
  archivo1.write(str(c)+'\n')
  archivo1.write(d+'\n')
  archivo1.close()
def cargarcuenta():
  archivo1= open('E_cuentatradergestor.txt', 'r')
  dinCta = float(archivo1.readline())
  riskCta = int(archivo1.readline())
  perdidasacep = float(archivo1.readline())
  archivo1.close()
  return dinCta,riskCta,perdidasacep
def cargarcuenta2():
  nombre = raw_input('CARGAR CUENTA NOMBRE:  ')
  cargarcuenta3(nombre)
  nombre = nombre+'.user'
  if existe_archivo(nombre):
    archivo1= open(nombre, 'r')
    dinCta = float(archivo1.readline())
    riskCta = int(archivo1.readline())
    perdidasAcep = float(archivo1.readline())
    archivo1.close()
    copiarcuenta(dinCta,riskCta,perdidasAcep,nombre)
    print('Cuenta cargada')
    return dinCta,riskCta,perdidasAcep
  else:
    print('No se verifica el nombre')
    return 
def cargarcuenta3(nombre):
  if existe_archivo(nombre+'.user'):
    archivo1= open(nombre+'.user', 'r')
    dinCta = float(archivo1.readline())
    riskCta = int(archivo1.readline())
    perdidasAcep = float(archivo1.readline())
    archivo1.close()
    print('Datos de la cuenta:\n\tDinero en cuenta = ',dinCta,'\n\triesgo cuenta [%] = ',riskCta,'\n\tUnidad de riesgo = ',perdidasAcep,'\n')
    return 
  else:
    print('No se verifica el nombre')
    return 
def registro(nombre):
  archivo1 = open('E_registrocuentas.txt','a')
  archivo1.write(nombre+'\n')
  archivo1.close()
def leer_registro():
  archivo1 = open('E_registrocuentas.txt','r')
  datos = archivo1.read()
  archivo1.close()
  print('Cuentas:\n\n',datos)
def existe_archivo(ruta):
    return os.path.isfile(ruta)

def type_trade():
  opcion = 1
  while opcion !=0:
    msj = """Seleccione tipo de operacion:
    1) Trade LONG
    2) Trade SHORT
    0) Salir    
    """
    opcion = check_opcion2_str(msj,2)
    return opcion

def TPSL():
  print('TakeProfit y StopLoss PORCENTUALES.\n(Enter para continuar)')
  TP1 = raw_input('TP [%] = ')
  SL1 = raw_input('SL [%] = ')#False porcentual
  print('TakeProfit y StopLoss en el PRECIO.')
  TP2 = raw_input('TP [USD] = ')
  SL2 = raw_input('SL [USD] = ')#True por unidad
  if SL1 == '':
    SL = float(SL2)
    SLtype = True
  elif SL2 == '':
    SL = float(SL1)
    SLtype = False
  else:
    print('Error SL. Dos valores entrados. Se selecciona la opcion porcentual')
    SL = float(SL1)
    SLtype = False
  if TP1 == '':
    TP = float(TP2)
    TPtype = True
  elif TP2 == '':
    TP = float(TP1)
    TPtype = False
  else:
    print('Error TP: dos valores entrados. Se selecciona la opcion porcentual')
    TP = float(TP1)
    TPtype = False
  return TP,SL,TPtype,SLtype
def obtener_precio(precioE,SL,TP,type,TPtype,SLtype):  
  if type == 1:
    if SLtype == False:
      precioSL= precioE*(1-SL/100)
      RBSL = SL
    elif SLtype == True:
      precioSL = SL
      RBSL = (1 - precioSL/precioE) * 100
    if TPtype == False:
      precioTP= precioE*(1+TP/100)
      RBTP = TP
    elif TPtype == True:
      precioTP = TP
      RBTP = (precioTP/precioE - 1) * 100
  elif type == 2:
    if TPtype == False:
      precioTP= precioE*(1-TP/100)
      RBTP = TP
    elif TPtype == True:
      precioTP = TP
      RBTP = (1 - precioTP/precioE) * 100
    if SLtype == False:
      precioSL= precioE*(1+SL/100)
      RBSL = SL
    elif SLtype == True:
      precioSL = SL
      RBSL = (precioSL/precioE - 1) *100
  RB = RBTP/RBSL
  return precioSL, precioTP, round(RB,2)

def volumenoperacion(total):
  X = int(raw_input('Porcentaje operativo de la cuenta[%]= '))
  Y = total * X/100
  return Y

def apalancamiento(volumenreal, perdidasacep, pE, pSL,type):
  continuar = True
  while(continuar):
    for i in range(1,21):
      volumenapal = volumenreal *i
      cantMon = volumenapal / pE
      if type == 1:
        perdidasapal = volumenapal - cantMon*pSL
      elif type == 2:
        perdidasapal = cantMon*pSL - volumenapal
      if perdidasapal >= perdidasacep:
        print('\t---------------------\n\t Apalancamiento x',i,'\n\t---------------------')
        return i
    print('20x queda chico, revisar  porcetaje de la cuenta.')
    continuar = bool(0)
  apal = 0
  print('Error apalancamiento = 0')
  return apal

def cantidadmonedas(volOp,pE,apal):
  cantMon = volOp * apal / pE
  cantDin = volOp * apal
  print('\t-------------------------------' )
  print('\tCantidad de monedas = ',round(cantMon,4),'\n\tDinero en la operacion = ',cantDin)
  print('\t-------------------------------\n'  )
  return round(cantMon,4)

def volOp_apal(dinCta,perdidasAcep,pE,pSL,type):  
  volOp = volumenoperacion(dinCta)
  apal = apalancamiento(volOp,perdidasAcep,pE,pSL,type)    
  while apal == 0:
    volOp = volumenoperacion(dinCta)
    apal = apalancamiento(volOp,perdidasAcep,pE,pSL,type)
  liq = precio_liquidacion(apal,pE,type)
  if type == 1:
    while liq > pSL:
      print(('Error: precio SL por debajo del precio liquidacion'))
      volOp = volumenoperacion(dinCta)
      apal = apalancamiento(volOp,perdidasAcep,pE,pSL,type)    
      liq = precio_liquidacion(apal,pE,type)
      print('SL por debajo de precio liquidacion')
  if type == 2:
    while liq < pSL:
      print(('Error: precio SL por encima del precio liquidacion'))
      volOp = volumenoperacion(dinCta)
      apal = apalancamiento(volOp,perdidasAcep,pE,pSL,type)    
      liq = precio_liquidacion(apal,pE,type)
      print('SL por encima de precio liquidacion')

  print('Volumen de operacion = ',volOp  )
  print('Precio de liquidaci�n = ',liq)
  cantMon = cantidadmonedas(volOp,pE,apal)
  return volOp,apal,liq,cantMon

def agregar_entrada(pE,cantMon):
  precio = [pE]
  volumen = []
  elemento = float(raw_input('Nueva entrada = '))
  msj = 'Desea ingresar una entrada promediada?'
  opcion = check_opcion_str(msj)
  if opcion == 1:
    elemento2 = round((pE+elemento)/2,2)
    precio.append(elemento2)
    precio.append(elemento)
    cantMon /= 3
    print()
  else:
    precio.append(elemento)
    cantMon /= 2
    print()
  for i in range(len(precio)):
    vol = round(cantMon * precio[i],2)
    volumen.append(vol)
  print('precio\tvolumen apal')
  for i in range(len(precio)):
    print(precio[i],'\t ',volumen[i])
  print('- - - - - - - - - - - - - - - - - - - - -\nCantidad de monedas por entrada = ',round(cantMon,4))
  return precio, volumen, cantMon

def precio_liquidacion(apal,pE,type):###si 20x queda chico no existe apal
  X = pE / apal
  if type == 1:
    Y = pE - X
  elif type == 2:
    Y = pE + X
  return round(Y,4)

def lista_volumenes(entrada,volumen,pTP,pSL):
  z_cantMon_l = []
  z_vol_TP_l = []
  z_vol_SL_l = []
  z_result_vol = []
  z_sum = 0.0
  for i in range(len(volumen)):
    z_sum += volumen[i]
  z_result_vol.append(z_sum)
  z_sum = 0.0
  for i in range(len(entrada)):
    z_cantMon_i = volumen[i]/entrada[i]
    z_sum += z_cantMon_i
    z_cantMon_l.append(z_cantMon_i)
  z_sum = 0.0
  for i in range(len(z_cantMon_l)):
    z_vol_TP_i = z_cantMon_l[i] * pTP
    z_sum += z_vol_TP_i
    z_vol_TP_l.append(z_vol_TP_i)
  z_result_vol.append(z_sum)
  z_sum = 0.0
  for i in range(len(z_cantMon_l)):
    z_vol_SL_i = z_cantMon_l[i] * pSL
    z_sum += z_vol_SL_i
    z_vol_SL_l.append(z_vol_SL_i)
  z_result_vol.append(z_sum)
  return z_result_vol#,cantMon_l,vol_TP_l,vol_SL_l

def RB_corregido(result_vol,type):
  vol_E = result_vol[0]
  vol_TP = result_vol[1]
  vol_SL = result_vol[2]
  if type == 1:
    porcentaje_superior = (vol_TP/vol_E) - 1
    porcentaje_inferior = 1 - (vol_SL/vol_E)
    RB = porcentaje_superior / porcentaje_inferior
    return round(RB,2)
  elif type == 2:
    porcentaje_superior = 1 - (vol_SL/vol_E)
    porcentaje_inferior = (vol_TP/vol_E) - 1
    RB = porcentaje_inferior / porcentaje_superior
    return round(RB,2)

def check_opcion_str(msj):
  continuar = True
  while continuar:
    print(msj)
    opcion = raw_input('(1:Si/0:No) >> ')
    if bool(opcion) == False:
      if opcion == '':
        print('opcion no valida\n')
      else:
        print('opcion no reconocida\n')
    elif bool(opcion) == True:
      if opcion == '1':
        return 1
      elif opcion == '0':
        return 0
      else:
        print('Opcion no reconocida\n')

def check_opcion2(msj,num):
  print(msj)
  opcion = int(raw_input('Elija una opcion >> '))
  while opcion < 0 or opcion > num:
    print(msj)
    opcion = int(raw_input('Elija una opcion >> '))
  return opcion

def check_opcion2_str(msj,num):
  continuar = True
  print(msj)
  while continuar:
    opcion = raw_input('>> ')
    if bool(opcion) == True:
      if opcion == '1':
        return 1
      elif opcion == '2':
        if num < 2:
          print('Opcion no valida\n')
        else:
          return 2
      elif opcion == '3':
        if num < 3:
          print('Opcion no valida\n')
        else:
          return 3
      elif opcion == '4':
        if num < 4:
          print('Opcion no valida\n')
        else:
          return 4
      elif opcion == '5':
        if num < 5:
          print('Opcion no valida\n')
        else:
          return 5
      elif opcion == '6':
        if num < 6:
          print('Opcion no valida\n')
        else:
          return 6
      elif opcion == '0':
        return 0
      else:
        print('Opcion no reconocida\n')
    elif bool(opcion) == False:
      if opcion == '':
        print('Opcion no valida\n')
      else:
        print('Opcion no reconocida\n')

def check_opcion4():
  opcion = raw_input('>> ')
  while opcion == '':
    return False
  return opcion

def archivo_enumerador(): #probablemente haya un return para crear titulos
  archivo1 = open('E_enumerador.txt','r')
  data1 = archivo1.read()
  data1 = int(data1)
  data1 += 1
  archivo1.close()
  archivo2 = open('E_enumerador.txt','w')
  if data1 < 10:
    data1 = str(data1)
    archivo2.write('00'+data1)
  elif data1 < 100:
    data1 = str(data1)
    archivo2.write('0'+data1)
  else:
    data1 = str(data1)
    archivo2.write(data1)
  archivo2.close()
  
def leer_enumerador():
  archivo1 = open('E_enumerador.txt','r')
  data1 = archivo1.readline()
  archivo1.close()
  return data1

def leer_linea(x):
  archivo1 = open('E_cuentatradergestor.txt','r')
  for i in range(x):
    data1 = archivo1.readline().rstrip()
  archivo1.close()
  return data1
def guardar_operacion(leer,lista):
  archivo1 = open(leer+'.txt','w')
  for elemento in lista:
    cadena = ''.join(elemento) 
    data1 = archivo1.write(cadena+'\n')
  archivo1.close()
def guardar_operacion2(leer,lista):
  archivo1 = open(leer+'.txt','a')
  for elemento in lista:
    cadena = ' '.join(elemento) 
    data1 = archivo1.write(cadena+'\n')
  archivo1.close()
def guardar_titulo(leer,lista):
  archivo1 = open(leer+'.txt','w')
  cadena = ' '.join(lista)
  data1 = archivo1.write(cadena+'\n')
  archivo1.close()

def reiniciar_enumerador():
  archivo1 = open('E_enumerador.txt','w')
  data1 = archivo1.write('000')
  archivo1.close()
  return
def reiniciar_registrocuentas():
  archivo1 = open('E_registrocuentas.txt','w')
  archivo1.close()
  return

def ingresar_temporalidad():
  a = raw_input('Temporalidad:\n>> ')
  return a

def ingresar_criterio():
  c = []
  a = raw_input('Criterios:\t(doble enter para volver)\n>> ')
  c.append('*'+a)
  check = check_opcion4()
  if check == False:
    check = check_opcion4()
  while bool(check):
    c.append('*'+check)
    while bool(check):
      check = check_opcion4()
      if bool(check) == True:
        c.append('*'+check)
      else:
        check = check_opcion4()
  return c

def agregar_linea(linea):
  archivo1 = open('E_cuentatradergestor.txt','a')
  data1 = archivo1.write(linea+'\n')
  archivo1.close()
def quitar_linea(): ## esta funcion limpia el archivo tradergestor. pero deberia cargarse desde la info del usuario por cada sesion abierta
  archivo1 = open('E_cuentatradergestor.txt','r')
  linea1 = archivo1.readline()
  linea2 = archivo1.readline()
  linea3 = archivo1.readline()
  linea4 = archivo1.readline()
  archivo1.close()
  archivo2 = open('E_cuentatradergestor.txt','w')
  data1 = archivo2.write(linea1)
  data2 = archivo2.write(linea2)
  data3 = archivo2.write(linea3)
  data5 = archivo2.write(linea4)
  archivo2.close()
  
def precio_promedio(entrada_l,cantMon_l):
  sum1 = 0.0
  sum2 = 0.0
  for i in range(len(entrada_l)):
    sum1 += entrada_l[i]*cantMon_l[i]
    sum2 += cantMon_l[i]
  precio_prom = sum1/sum2
  return round(precio_prom,4)

#><><><><><><><><><><><><><><><><                    ><><><><><><><><><><><><><><><>< 
#><><><><><><><><><><><><><><><>< PROGRAMA PRINCIPAL ><><><><><><><><><><><><><><><><
#><><><><><><><><><><><><><><><><                    ><><><><><><><><><><><><><><><><
op = menu()
while op != 0:
  
#--------------> FUNCION 1 <--------------#
  if op == 1: 
    opcion = menu1()
    while opcion != 0:

      if opcion == 1:
        print('\n\t> Crear Cuenta <')
        (dinCta, riskCta, perdidasAcep) = crearcuenta()
        opcion = menu1()

      elif opcion == 2:
        print('\n\t> Registro de cuentas <\n')
        leer_registro()
        leer = int(raw_input('(1:Si/0:No) Desea leer los datos? '))
        if leer < 0 or leer > 1:
          while leer < 0 or leer > 1:
            leer = int(raw_input('(1:Si/0:No) Desea leer los datos? '))
            if leer == 1:
              elemento = raw_input('LEER CUENTA NOMBRE: ')
              cargarcuenta3(elemento)
              break
            elif leer == 0:
              break
        elif leer == 1:
          elemento = raw_input('\nLEER CUENTA NOMBRE: ')
          cargarcuenta3(elemento)
        opcion = menu1()

      elif opcion == 3:
        print('\n\t> Actualizar cuenta <\n') #corregir bucle)
        leer_registro()
        (dinCta, riskCta, perdidasAcep) = crearcuenta2()
        opcion = menu1()
        if dinCta == False and riskCta == False and perdidasAcep == False:
          print('error al cargar')
          opcion = menu1()

      elif opcion == 4:
        print('\n\t> Cargar cuenta <\n')
        leer_registro()
        (dinCta, riskCta, perdidasAcep) = cargarcuenta2()
        opcion = menu1()
    op = menu()
    
#--------------> FUNCION 2 <--------------#
  elif op == 2: 
    print('\n\n \t> ABRIR OPERACION <\n')
    (dinCta, riskCta, perdidasAcep) = cargarcuenta()
    print('Datos de la cuenta:\n\tDinero en cuenta = ',dinCta,'\n\triesgo cuenta [%] = ',riskCta,'\n\tUnidad de riesgo = ',perdidasAcep,'\n')
    print('Cuenta: ',leer_linea(4),'\n')
    type = type_trade()
    if type == 0:
      print('Operaci�n abortada')
    elif type == 1 or type == 2:
      msj = """\nSeleccion tipo de orden:
      1) Orden PENDIENTE
      2) Orden ABIERTA
      3) Orden EJECUTADA
      0) Salir
"""
      opcion = check_opcion2_str(msj,3)

      if opcion == 0:
        print('Operacion abortada')
     
      elif opcion == 3:
        linea5 = 'RUN'
        
        linea6 = 'ESTADO 3 = EJECUTADA '
##        msj = """\nSeleccione una opcion:
##          1) APERTURA de posicion
##          2) CIERRE de posicion
##          0) Volver
##"""
##        type_run = check_opcion2(msj,2)
##
##        if type_run == 1: ###esto lo quiero sacar
##          linea6 += 'APERTURA POSICION- '
##          elemento = raw_input('proviene de: ')
##          linea6 += 'Proviene de: ' + elemento
##        elif type_run == 2:
##          linea6 += 'CIERRE POSICION- '
##          elemento = raw_input('Proviene de: ')
##          linea6 += 'Proviene de: ' + elemento
        agregar_linea(linea5)
        agregar_linea(linea6)
        
        leer = 'A'
        lista = []
        lista1 = []
        lista2 = []
        lista3 = []
        
        archivo_enumerador()
        sum = leer_enumerador()
        lista.append([sum])
        leer += sum + '_'
        
        i = 6 #estado
        elemento = leer_linea(i) 
        lista.append([elemento])

        
        i = 4 #cuenta
        elemento = leer_linea(i)
        lista.append(['Cuenta: '+elemento])
        lista.append([])
        lista.append(['Moneda\tTipo\tFecha\tRB\tHora\tUnidad de riesgo'])
#arranca modificacion
        print('\n\t> Ingresar entradas <')
        apal = int(raw_input('Apalancamiento = '))
        lista3.append('i   Entrada\tVol Apalancado\tCant Monedas\n')

        continuar = True
        sum1 = 0 #contador
        sum2 = 0.0 #cantidad de monedas
        sum3 = 0.0 #volumen operado
        entrada_l = []
        cantMon_l = []
        volumen_l = []
        while continuar:
          sum1 += 1
          elemento = float(raw_input('Entrada = ')) #
          elemento2 = float(raw_input('Cantidad de monedas = '))#
          entrada_l.append(elemento)
          cantMon_l.append(elemento2)
          sum2 += elemento2
          volumen_i = apal* elemento* elemento2
          volumen_l.append(volumen_i) #volumen por orden entrada
          sum3 += volumen_i
          msj = '\nNueva entrada?'
          check = check_opcion_str(msj)
          elemento = str(round(elemento,4))
          elemento2 = str(elemento2)
          volumen_i = str(volumen_i)
          elemento = str(sum1) +'.  '+ elemento +'\t'+volumen_i+'\t\t'+elemento2 ##tabla1
          lista3.append(elemento+'\n')
          if check == 0:
            continuar = False
            cantMon = sum2
            volApal = round(sum3,2)
            volOp = sum3/apal

        precio_prom_e = precio_promedio(entrada_l,cantMon_l)
  
        lista3.append('\ni  Precio SL\tPrecioTP\t%Destinado\tCant Monedas\tPerdidas\tGanancias\n')
        print('\n\t> Definir Targets <') #)
        continuar = True
        sum1 = 0
        sum2 = 100.0
        sum3 = 0.0 #perdidas totales
        sum4 = 0.0 #ganancias totales
        pSL_l = []
        pTP_l = []
        QMon = []
        while continuar:
          pSL = float(raw_input('Precio Stop Loss = '))#
          pTP = float(raw_input('Precio Take Profit = '))#
          pSL_l.append(pSL)
          pTP_l.append(pTP)
          porc_dest = raw_input('Porcentaje Destinado [%] = ')#
          if porc_dest == '':
            cantMon_i = float(raw_input('Cantidad de monedas = '))#
            porc_dest = round(cantMon_i/cantMon *100,1)
          else:
            porc_dest = round(float(porc_dest),1)
          cantMon_i = round(cantMon*porc_dest/100,4)
          QMon.append(cantMon_i)
          if sum2 - porc_dest >= 0:
            sum1 += 1
            elemento = str(sum1)+'.  '+str(pSL)+'\t'+str(pTP)+'\t\t'+str(porc_dest)+'%\t\t'+str(cantMon_i)+' Un.' ##check
            sum2 -= porc_dest
            if type == 1: #LONG
              elemento2 = round((precio_prom_e-pSL)*cantMon_i,2)
              sum3 += elemento2
              elemento += '\t'+str(elemento2)
              elemento2 = round((pTP-precio_prom_e)*cantMon_i,2)
              sum4 += elemento2
              elemento += '\t\t'+str(elemento2)
            elif type == 2: #SHORT
              elemento2 = round((pSL-precio_prom_e)*cantMon_i,2)
              sum3 += elemento2
              elemento += '\t'+str(elemento2)
              elemento2 = round((precio_prom_e-pTP)*cantMon_i,2)
              sum4 += elemento2
              elemento += '\t\t'+str(elemento2)
            lista3.append(elemento+'\n')
          else:
            print('Queda disponible ',sum2,'%\nVuelva a intentarlo')
          if sum2 > 0:
            msj = '\nCargar nuevos targets?'
            check = check_opcion_str(msj)
            if check == 0:
              continuar = False
              sum1 += 1
              cantMon_i = round(cantMon*sum2/100,4)
              elemento = str(sum1)+'.  \t\t\t\t'+str(sum2)+'%\t\t'+str(cantMon_i)+' Un.'
              lista3.append(elemento)
          else:
            continuar = False

        tot_perd = sum3
        tot_gan = sum4
        precio_prom_p = precio_promedio(pSL_l,QMon)
        precio_prom_g = precio_promedio(pTP_l,QMon)
        volTP = cantMon * precio_prom_g
        volSL = cantMon * precio_prom_p
        volumen_RB = [volOp,volTP,volSL]
        RB = RB_corregido(volumen_RB,type)
              
## arranca lista 1
        print('\n\t> Datos del Trade <')
        elemento = raw_input('Nombre del par =  ')
        leer = leer + elemento.upper() + '_'#leer
        elemento = elemento + '\t'
        lista1.append(elemento.upper())
        if type == 1:
          elemento = 'LONG\t'
        elif type == 2:
          elemento = 'SHORT\t'
        lista1.append(elemento)
        elemento = raw_input('La fecha del dia? (2 numeros): ')
        elemento2 = raw_input('El corriente mes? (3 letras): ')
        elemento2 = elemento2.upper()
        elemento += elemento2
        leer = leer + elemento + '_' #leer
        elemento += '\t'
        lista1.append(elemento)
        elemento = str(RB)
        elemento += '\t'
        lista1.append(elemento)

        elemento = raw_input('Indica solo la Hora:  ')
        elemento2 = raw_input('Ahora indica los minutos: ')
        elemento = elemento + ':' + elemento2
        elemento += '\t'
        lista1.append(elemento)
        elemento2 = str(perdidasAcep)
        elemento = elemento2 + 'usd\n'
        lista1.append(elemento)
        i = 5
        leer += leer_linea(i)


        elemento = 'Monto_cuenta: '
        elemento2 = str(dinCta)
        elemento += elemento2
        lista2.append(elemento)
        elemento = ' Ganancias_tot: '+str(tot_gan)
        lista2.append(elemento)
        elemento = ' Perdidas_tot: '+str(tot_perd)
        lista2.append(elemento)
        elemento = '\nApalancamiento: '
        elemento2 = str(apal)
        elemento += elemento2
        lista2.append(elemento)
        elemento = ' Cantidad_monedas: '
        elemento2 = str(cantMon)##########
        elemento += elemento2
        lista2.append(elemento)
        elemento = ' Volumen_operado : '+str(round(volOp,1))
        lista2.append(elemento+'\n')####################

        print('\nTrade guardado N ',sum, '\n')
        lista.append(lista1) # quinta linea lista
        lista.append(lista2)
        lista.append(lista3)
        guardar_operacion(leer,lista)
        quitar_linea()        
          

        






        ### fin del estado 3 = run
        
      elif opcion == 1 or opcion == 2:
        if opcion == 1:
          linea5 = 'PEND'
          linea6 = 'ESTADO 1 = PENDIENTE'
          agregar_linea(linea5)
          agregar_linea(linea6)
        elif opcion == 2:
          linea5 = 'OPEN'
          linea6 = 'ESTADO 2 = ABIERTA'
          agregar_linea(linea5)
          agregar_linea(linea6)

        print('\n\n\t> Precio entrada y targets <\n\n')
        pE= float(raw_input('Precio de entrada = '))
        (TP,SL,TPtype,SLtype) = TPSL()
        (pSL, pTP,RB) = obtener_precio(pE,SL,TP,type,TPtype,SLtype)
        print('\t----------------------------')
        print("\t\tR:B ", round(RB,2),)
        print('\n\t\tprecioTP = ', round(pTP,4),'\n\t\tprecioSL = ',round(pSL,4), )
        print('\n\t----------------------------\n')
        print('\n\n\t> Volumen operado y apalancamiento <\n\n')
        (volOp,apal,liq,cantMon) = volOp_apal(dinCta,perdidasAcep,pE,pSL,type)


        msj = 'Quiere agregar una entrada?'
        check = check_opcion_str(msj)
        if check == 1:
         (entrada,volumen,cantMon) = agregar_entrada(pE,cantMon) #cantidad de moneda por entrada
         result_vol = lista_volumenes(entrada,volumen,pTP,pSL)
         RB = RB_corregido(result_vol,type)
       
        else:
          entrada = [pE]
          volumen = [volOp*apal]

################################################################
### GUARDAR, DESEA CORREGIR LA OPERACION ANTES DE GUARDARLA? ###
################################################################

        print('\n\n\t> Guardar operacion < \n\n')
        msj = 'Desea guardar la operacion?'
        opcion = check_opcion_str(msj) 

        if opcion == 1:
          prin()
          leer = 'A' #leer nombre archivo, identificador funcion 2
          lista = [] # lista global
          lista1 = [] #lista1 datos operacion
          lista2 = [] #lista2 estado operacion
          lista3 = [] #lista3 resultado operacion
          archivo_enumerador()
          sum = leer_enumerador()
          lista.append([sum]) #lista 0 contiene, enumerador formato int
          leer = leer + str(sum) +'_' #leer
          i = 6
          elemento = leer_linea(i)
          lista.append([elemento])
          i = 4
          elemento = leer_linea(i)
          lista.append(['Cuenta: '+elemento])
          lista.append([])
          lista.append(['Moneda\tTipo\tFecha\tRB\tHora\tUnidad de riesgo'])
#LISTA1: LINEA 6 DE LISTA
          elemento = raw_input('Introduzca el nombre de la moneda =  ')
          leer = leer + elemento.upper() + '_'#leer
          elemento = elemento + '\t'
          lista1.append(elemento.upper())
          if type == 1:
            elemento = 'LONG\t'
          elif type == 2:
            elemento = 'SHORT\t'
          lista1.append(elemento)
          elemento = dt.date.today()
          elemento2 = raw_input('El corriente mes? (3 letras): ')
          elemento2 = elemento2.upper()
          elemento += elemento2
          leer = leer + elemento + '_' #leer
          elemento += '\t'
          lista1.append(elemento)
        
          elemento = str(RB)
          elemento += '\t'
          lista1.append(elemento)

          elemento = raw_input('Indica solo la Hora:  ')
          elemento2 = raw_input('Ahora indica los minutos: ')
          elemento = elemento + ':' + elemento2
          elemento += '\t'
          lista1.append(elemento)
          elemento2 = str(perdidasAcep)
          elemento = elemento2 + 'usd\n'
          lista1.append(elemento)
          i = 5
          leer += leer_linea(i)

#LISTA2: LINEA 7 DE LISTA
          elemento = 'Monto_cuenta: '
          elemento2 = str(dinCta)
          elemento += elemento2
          lista2.append(elemento)
          if type == 1:
            elemento = ' Posibles_ganancias: '
            elemento3 = 0.0
            for i in range(len(entrada)):
              elemento2 = (pTP-entrada[i])*cantMon
              elemento3 += elemento2
            elemento3 = str(round(elemento3,2))  
            elemento += elemento3
            lista2.append(elemento)
            elemento = ' Posibles_perdidas: '
            elemento3 = 0.0
            for i in range(len(entrada)):
              elemento2 = (entrada[i]-pSL)*cantMon
              elemento3 += elemento2
            elemento3 = str(round(elemento3,2))
            elemento += elemento3
            lista2.append(elemento)
 
          elif type == 2:
            elemento = ' Posibles_ganancias: '
            elemento3 = 0.0
            for i in range(len(entrada)):
              elemento2 = (entrada[i]-pTP)*cantMon
              elemento3 += elemento2
            elemento3 = str(round(elemento3,2))
            elemento += elemento3
            lista2.append(elemento)
            elemento = ' Posibles_perdidas: '
            elemento3 = 0.0
            for i in range(len(entrada)):
              elemento2 = (pSL-entrada[i])*cantMon
              elemento3 += elemento2
            elemento3 = str(round(elemento3,2))
            elemento += elemento3
            lista2.append(elemento)

          elemento = '\nApalancamiento: '
          elemento2 = str(apal)
          elemento += elemento2
          lista2.append(elemento)
          elemento = ' Cantidad_monedas: '
          elemento2 = str(cantMon*len(entrada))
          elemento += elemento2
          lista2.append(elemento)
          elemento = ' Volumen_operado : '
          if len(entrada) == 1:
            elemento2 = str(volOp)
          else:
            elemento3 = 0.0
            for i in range(len(volumen)):
              elemento2 = volumen[i]/apal
              elemento3 += elemento2
            elemento2 = str(elemento3)
          elemento += elemento2
          lista2.append(elemento)
#LISTA3 : 
          lista3.append('\nEntrada \tVolumen apalancado \tCantidad de monedas\n')
          for i in range(len(entrada)):
            elemento = str(entrada[i])+'\t\t'+str(volumen[i])+'\t\t\t'+str(round(cantMon,5))+'\n'
            lista3.append(elemento)
          lista3.append('\n\nPrecio Stop Loss\tPrecio Take Profit\n')
          elemento = str(pSL)+'\t\t\t'+str(pTP)
          lista3.append(elemento)

          print('\nTrade guardado N ',sum, '\n')
          lista.append(lista1) # quinta linea lista
          lista.append(lista2)
          lista.append(lista3)
          guardar_operacion(leer,lista)
          quitar_linea()
        


    op = menu()

#--------------> FUNCION 3 <--------------#
  if op == 3:
    msj = """\nARCHIVOS DE TEXTO:
    1) Trade Daily Note
    2) Trade Daily Work
    0) Volver    
"""
    opcion = check_opcion2_str(msj,2)
    continuar = True
    while continuar:
      
      if opcion == 1:
        lista = []
        temporalidad = []
        criterio = []
        elemento = raw_input('Divisa: ')
        elemento = elemento.upper()
        i = raw_input('Indice: ')
        elemento2 = raw_input('Nota Numero: ')
        elemento3 = raw_input('Fecha: ')
        elemento3 = elemento3.upper()
        leer = 'N'+i+'_'+elemento2+'_'+elemento+'_'+elemento3+'.txt'

        titulo = [elemento,'\n'+elemento3,'\nProviene de:'] 

        temporalidad.append(ingresar_temporalidad())
        criterio.append(ingresar_criterio())
        msj2 = 'Otra temporalidad? '
        check = check_opcion_str(msj2)
        while check == 1:
          temporalidad.append(ingresar_temporalidad())
          criterio.append(ingresar_criterio())
          check = check_opcion_str(msj2)
        for i in range(len(temporalidad)):
          lista.append(['\nTEMPORALIDAD:\t'+temporalidad[i]])
          for j in range(len(criterio[i])):
            lista.append([criterio[i][j]])


        guardar_titulo(leer,titulo)
        guardar_operacion2(leer,lista)
        print('Fin funcion\n')
        opcion = check_opcion2(msj,2)
        
      elif opcion == 2:
        print('En desarollo aun')
        opcion = check_opcion2(msj,2)
      elif opcion == 0:
        print('Ha elegido volver.\n')
        continuar = bool(0)
      else:
        print('Opcion no reconocida.\n')
        continuar = bool(0)

    op = menu()
#--------------> FUNCION 4 <--------------#
  if op == 4:
    msj ="""\nCONFIGURACION:
    1) Reiniciar contador de trades
    2) Reiniciar registro de cuentas
    0) Volver
"""
    opcion = check_opcion2_str(msj,2)
    if opcion == 1:
      reiniciar_enumerador()
      print('\nContador reiniciado\n')

    elif opcion == 2:
      reiniciar_registrocuentas()
      print('\nRegistro reiniciado\n')

    elif opcion == 0:
      op = menu()
    else:
      op = menu()
#-------------->   SALIR   <--------------#
#  if op == 0:
print('\n\nCualquier aporte o solicitud puede hacerla comunicandose a traves del mail jackone.action.software@gmail.com\nMuchisimas gracias por usar el programa.')
raw_input('\nFIN TraderGestorDEMO ---> Enter para salir')
print('Esperamos haber sido de utilidad en su trading.')
